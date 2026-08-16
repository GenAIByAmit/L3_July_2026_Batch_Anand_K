# Zensar L3 — Quick Revision Notes (Weak Areas)

Targeted notes for the concepts you missed in the first practice set. Read each section, then attempt `practice_questions-2.md`.

---

## 1. Tool calling & agent state

- **`llm.bind_tools(tools)`** attaches the tool schemas to the model so it can *emit structured tool calls*. `invoke()` just sends a prompt — it never "passes tools".
- **`@tool`** on a plain function generates the JSON schema the LLM sees:
  - name → function name
  - args → Python **type annotations**
  - description → **docstring** (what tells the LLM when/how to call it)
- **`create_agent(model, tools, system_prompt)`** returns a compiled LangGraph ReAct agent: `assistant → tools → assistant` loop that stops automatically.
- **Agent state key is always `"messages"`** (a list).
  - Input: `{"messages": [{"role": "user", "content": "..."}]}`
  - Output: `result["messages"]` with the final `AIMessage` last.
- Invalid tool call → the error is fed back to the model as a message so it can recover (no crash).

## 2. LangGraph internals

- **State = a shared dict** (defined with `TypedDict`). Every node receives the current state.
- **Nodes return a PARTIAL dict** that gets **merged** into the state — only the returned keys update. Never return a "full replacement".
- **Appending** to a list key needs a **reducer**: `Annotated[list, operator.add]` (or `add_messages`). Without it, each node **overwrites** the key.
- **Edges**: `add_edge` (fixed), `add_conditional_edges` (route based on state). Entry/exit = `START` / `END`. Compile with `.compile()` before use.
- **Tool loop**: assistant node → conditional edge → if last AI message has `tool_calls` → `ToolNode` executes them → back to assistant; else → `END`.
- **Parallelism**: nodes run in parallel only when they touch **disjoint keys** (no data dependency). Fan-out = one node splits to N workers; fan-in = merge their updates back.
- **Sub-graph**: a compiled graph added as a node. Parent passes state in via node-name mapping; sub-graph returns state updates. Great for reuse + validation (validator returns a `valid/invalid` flag the parent routes on).
- `graph.stream(...)` → intermediate events; `graph.invoke(...)` → final state.

## 3. Long-term memory

Two mechanisms — don't confuse them:

| | Checkpointer | Store |
|---|---|---|
| Example | `MemorySaver`, `SqliteSaver` | `InMemoryStore`, `SqliteStore` |
| Scope | **short-term**, per **`thread_id`** | **long-term**, keyed by **user namespace/id** |
| Holds | conversation state across turns | durable facts about the user, across sessions |
| Survives restart? | `MemorySaver` = No (in-memory) | `SqliteStore` = Yes (disk/DB) |

- Same agent instance can serve many users: each conversation is isolated by its own `thread_id`.
- **Agent self-managed memory**: memory tools using `get_store()` / `get_config()` from `langgraph.config` let the agent save/recall facts itself.

## 4. HITL — resume mechanism

- **`interrupt()`** in a node **pauses** the graph; state is **checkpointed under the `thread_id`**; control returns to the caller (human).
- **Resume**: invoke **again with the SAME `thread_id`** and pass `Command(resume=<value>)`. The value becomes the **return value of `interrupt()`** inside the node.
- Approve → graph resumes and executes the action. Reject → feedback is given to the model so it answers **without** doing the action (graceful degradation).
- Put approval gates **before irreversible / high-impact tools** (send email, payments). Record approvals → **audit trail** (compliance).
- HITL is a control-flow pattern — no UI strictly required; the "human" input can come from code.

## 5. MCP transports

- **Default transport = stdio**: the server runs as a subprocess; the client passes the **script path**: `Client("09_local_stdio_mcp_server.py")`.
- **streamable_http (shttp)**: server does `mcp.run(transport="http", port=8000)`; client connects to the URL, e.g. `http://localhost:8000/mcp`.
- **Hosted MCP (Tavily)**: HTTPS URL with the key in the query string — `?tavilyApiKey=...`.
- **Server must be listening before the client connects** ("connection refused" on :8000 ⇒ server not started).
- Primitives: `@mcp.tool` (actions), `@mcp.resource("book://{id}")` (data by URI), `@mcp.prompt` (templates).
- LangChain integration: `MultiServerMCPClient({"name": {"url": ..., "transport": "streamable_http"}})` → `get_tools()` → pass into the agent.

## 6. RAG pipeline

```
Load → Split → Embed → Index/Store → Retrieve → Generate
```

- **`RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)`**: 500-char chunks with 50-char **overlap** so context isn't lost at chunk boundaries.
- Chunks too large → embedding quality/retrieval relevance drop and context-window pressure grows.
- **Embeddings**: `OpenAIEmbeddings()` or `HuggingFaceEmbeddings(model_name="nomic-ai/nomic-embed-text-v1.5")`. Similar texts land close in vector space → **similarity search = retrieval signal**.
- **Stores**: `FAISS.from_documents(docs, embeddings)`, `Chroma.from_documents(chunks, embeddings)`.
- **MultiQueryRetriever**: LLM rewrites the question into several variants → more relevant chunks retrieved (**better recall**).
- **HyDE**: generate a *hypothetical passage that would answer the question*, embed it, retrieve — bridges the query-vs-document semantic gap.
- **`RetrievalQA` chain_type="stuff"**: all retrieved chunks are stuffed into the prompt as context. RAG reduces hallucination by **grounding answers in retrieved evidence**.

## 7. Guardrails — input vs output

- **Input guardrails (pre-model)**: PII redaction, API-key blocking, prompt-injection / harmful-content filtering, topic filters.
- **Output guardrails (post-model)**: LLM-as-judge `SAFE`/`UNSAFE` verdicts on generated text.
- **Deterministic (regex/rules)** = cheap & fast → run **first**; **model-based** = semantic judgment → run after.
- **`AgentMiddleware`** wraps **model and tool calls**; stack layers for defense-in-depth (redaction → topic → output safety → HITL approval).
- HITL approval gate for irreversible/high-impact tools.
- **Prompt injection** ("ignore your instructions"): treat user input as **untrusted data**; filter/validate it before it can influence tool flows.
- False positives hurt UX → tune thresholds; guardrails also validate **tool-call arguments** to block risky/injected invocations.

## 8. Repo ops gotchas

- **Ollama must run locally** with `gpt-oss:120b-cloud` pulled, or every notebook/script fails on localhost connection.
- Cloud keys (`OPENAI_API_KEY`, `TAVILY_API_KEY`, ...) live in a **repo-root `.env`** loaded via python-dotenv `find_dotenv()`.
- Corporate SSL errors → trust the **corporate proxy CA** (`certifi` / `pyOpenSSL` / `python-certifi-win32` in requirements).
- Capstone order: `mcp_shopping_server.py` (port 8000) → `agent_shopping.py` (connects to `localhost:8000/mcp`) → `agentic_chatbot.py` (Gradio 7860, imports `get_shopping_agent`).
- `agent_shopping.py` calls `asyncio.run()` **at module level** (lines 55–56) — importing the module triggers the call.

## 9. Drill — the 7 concepts you missed in Set 2

Read these, then try to explain each aloud from memory. (These are the exact Set-2 questions you got wrong.)

**1. What is a "channel" in LangGraph?**
A channel = **a key of the shared state** that nodes read and write (e.g. `messages`). It is *not* a network port, a log stream, or an LLM call. You define channels when you declare the state `TypedDict`.

**2. How do you wire fan-out to parallel workers?**
You connect **START (or a router node) → each worker node**. The workers are siblings, not a chain — they don't reach each other. Results are then merged at a fan-in node.
```
START ─┬─> worker1 ─┐
       ├─> worker2 ─┼─> combine
       └─> worker3 ─┘
```

**3. Does HITL need a web UI?**
**No.** HITL is a **control-flow pattern**: a node calls `interrupt()`, the graph *pauses*, and execution is checkpointed. The "human" input is just the value passed back in `Command(resume=...)` — it can come from code, a CLI, Gradio, anything. The UI is optional; the resume mechanism is what matters.

**4. What does `await client.call_tool("greet", {"name": "Tom"})` return?**
It returns **the tool's result content** (the output the server produced). It is *not* fire-and-forget — that's why the training code `print`s it. `list_tools()` returns the tool *definitions*; `call_tool` returns tool *results*.

**5. Which capstone file is the MCP server?**
Only **`mcp_shopping_server.py`** (FastMCP on port 8000). The other two are *clients* of it:
- `agent_shopping.py` → LangGraph agent, **connects to** the MCP server via `MultiServerMCPClient`
- `agentic_chatbot.py` → Gradio UI, imports the agent
One server, two consumers.

**6. Why does embedding similarity = retrieval?**
Embeddings put **texts with the same meaning close together in vector space**. So the distance between the *query* embedding and a *document chunk* embedding is exactly the retrieval signal: closest = most relevant. (It's not about compression or dedup.)

**7. What does a vector-store similarity search return?**
The **document chunks whose embeddings are most similar to the query embedding** — i.e. the top-k relevant chunks. It ranks your *chunks*, never tool outputs, raw models, or the whole corpus.

**Quick self-check (answers below):**
- a) `graph.invoke()` returns ___ (final state / token stream)
- b) Fan-out wires START/router → ___ (each worker / a chain)
- c) HITL input must come from a UI: ___ (true / false)
- d) `call_tool` returns the tool's ___ (schema / result content)
- e) The MCP server in the capstone is ___ (`mcp_shopping_server.py` / `agent_shopping.py`)
- f) Similarity search returns the ___ chunks (most similar / random)
- g) A channel is a ___ of shared state (key / log)

Answers: a) final state  b) each worker  c) false  d) result content  e) `mcp_shopping_server.py`  f) most similar  g) key
