# Zensar L3 AI — Practice Objective Questions (Set 2)

Second practice paper, covering the same curriculum as Set 1 but with all-new questions. Answer key at the bottom.

---

## 1. LLM Fundamentals & Tool Calling

1. To get a single response from a `ChatOllama` model you call:
   - A) `model.invoke("...")``                        '[Correct]'
   - B) `model.generate_all("...")`
   - C) `model.attach("...")`
   - D) `model.compile("...")`

2. In `create_agent`, what is the `system_prompt` used for?
   - A) To store the conversation history
   - B) To define the agent's role/behavior and how it should use tools`                        '[Correct]'
   - C) To set the model's temperature
   - D) To name the thread

3. Why is `@tool` placed on a plain Python function before passing it to an agent?
   - A) It makes the function run faster
   - B) It logs every call
   - C) It auto-generates the JSON schema (name, args, description) that the LLM sees`                        '[Correct]'
   - D) It caches results

4. Which part of a `@tool` function is turned into the tool's description for the LLM?
   - A) The return value
   - B) The function name only
   - C) The parameter defaults
   - D) The docstring`                        '[Correct]'

5. How does the agent decide which tool to call for a user request?
   - A) The LLM matches the request to the tool names/descriptions in the schema`                        '[Correct]'
   - B) It runs every tool and picks the first result
   - C) The user must pick the tool manually
   - D) Tools are called alphabetically

6. What typically happens when a model emits an invalid tool call in the graph?
   - A) It is silently ignored
   - B) The error is passed back to the model as feedback so it can recover`                        '[Correct]'
   - C) The whole app crashes
   - D) The model retrains

7. Built-in tools like DuckDuckGo search or Wikipedia are used to:
   - A) Replace the LLM entirely
   - B) Store conversation memory
   - C) Give the model access to up-to-date external information`                        '[Correct]'
   - D) Compress the prompt

8. Which class is used in the training to call Tavily's web search API as a tool?
   - A) `WikipediaQueryRun`
   - B) `DuckDuckGoSearchResults`
   - C) `SearchTool`
   - D) `TavilyClient``                        '[Correct]'

9. After `agent.invoke(...)`, where do you find the final assistant reply?
   - A) In `result["messages"]` as the last AIMessage`                        '[Correct]'
   - B) In `result["answer"]`
   - C) In `result["tool"]`
   - D) It is printed only

10. `temperature=0` on the chat model is used for:
    - A) More creative, varied output
    - B) More deterministic/reliable tool-calling behaviour`                        '[Correct]'
    - C) Faster network calls
    - D) Lowering token counts automatically

## 2. Agent Memory

11. After each agent turn, the updated conversation state is kept:
    - A) Only inside the LLM weights
    - B) In the vector store
    - C) In the checkpointer, keyed by `thread_id``                        '[Correct]'
    - D) Nowhere — it is lost

12. If you restart the Python process, which of these still has its data?
    - A) `MemorySaver`
    - B) `InMemoryStore`
    - C) The in-memory conversation list
    - D) `SqliteStore` (SQLite-backed)`                        '[Correct]'

13. The namespace (e.g., a user id) in a Store represents:
    - A) Who owns the long-term facts — scoping by user`                        '[Correct]'
    - B) Which tools are loaded
    - C) The model version
    - D) The thread's message count

14. The checkpointer stores state under a key derived from:
    - A) The system prompt hash
    - B) The `configurable.thread_id` in the config`                        '[Correct]'
    - C) The tool names
    - D) The model name

15. The memory-tools pattern (`get_store` / `get_config`) lets the agent:
    - A) Connect to MCP servers
    - B) Change its model at runtime
    - C) Save and recall durable facts about the user by itself`                        '[Correct]'
    - D) Reset the thread

16. Long-term memory (Store) is the right place for:
    - A) The full chat transcript of one conversation
    - B) Tool definitions
    - C) The system prompt
    - D) Durable user facts (preferences, profile) that should survive across sessions`                        '[Correct]'

17. Short-term memory answers "what was just said"; long-term memory answers:
    - A) "what do I know about this user across sessions"`                        '[Correct]'
    - B) "which tools exist"
    - C) "what is the temperature"
    - D) "how many tokens are used"

18. Why choose a SQLite/Postgres-backed memory instead of in-memory in production?
    - A) It makes the LLM faster
    - B) Data persists across restarts and can be shared by multiple processes`                        '[Correct]'
    - C) It needs no API key
    - D) It uses smaller models

19. One agent instance serving many users works because:
    - A) Each user gets a new model
    - B) The prompt is regenerated per user
    - C) Each user's conversation is isolated by its own `thread_id``                        '[Correct]'
    - D) It only supports one user

20. Which statement is TRUE about memory in this training?
    - A) Memory is embedded in the agent object itself
    - B) Long-term and short-term memory are the same thing
    - C) Memory requires a vector database
    - D) Memory is determined by how you call the agent (`thread_id`) and the store you attach`                        '[Correct]'

## 3. LangGraph Fundamentals

21. Before you can invoke a LangGraph, you must first:
    - A) Call `.compile()` on the StateGraph`                        '[Correct]'
    - B) Call `.train()`
    - C) Export a JSON file
    - D) Nothing — it runs immediately

22. Which pair of symbols marks the entry and exit of a graph?
    - A) IN / OUT
    - B) START / END`                        '[Correct]'
    - C) BEGIN / FINISH
    - D) TOP / BOTTOM

23. What does each node function receive as input?
    - A) Only the user's last message
    - B) The compiled tools
    - C) The current shared state (dict)`                        '[Correct]'
    - D) The final answer

24. What is a "channel" in LangGraph?
    - A) A network port
    - B) A log stream`                        '[Correct]'
    - C) An LLM call
    - D) A key of the shared state that nodes read/write

25. The "else" branch of a conditional edge (when there are no tool calls) typically routes:
    - A) Back to the assistant to continue the conversation, or to END`                        '[Correct]'
    - B) To a crash handler
    - C) To the tool node
    - D) To a restart

26. To fan out to several parallel worker nodes, you connect:
    - A) The worker nodes in a chain
    - B) START (or a router node) to each worker
    - C) Each worker to END only`                        '[Correct]'
    - D) A single loop node

27. A sub-graph communicates with the parent graph via:
    - A) Files on disk
    - B) HTTP calls
    - C) State mapping — parent passes selected keys in, sub-graph returns updates`                        '[Correct]'
    - D) Environment variables

28. Node A returns `{"count": 5}` and node B returns `{"status": "ok"}`. The merged state:
    - A) Loses `count`
    - B) Crashes
    - C) Duplicates both keys
    - D) Contains both keys`                        '[Correct]'

29. A good reason to use a conditional edge instead of a fixed edge:
    - A) Route differently based on runtime state (e.g., tool-call results)`                        '[Correct]'
    - B) The graph compiles faster
    - C) Fewer nodes are needed
    - D) It enables cloud sync

30. `graph.invoke(...)` with a config returns:
    - A) A token stream
    - B) The final state after execution`                        '[Correct]'
    - C) Only the model name
    - D) Nothing

## 4. Parallel Nodes, Sub-Graphs, & Multi-Agent

31. Fan-in combines parallel results by:
    - A) Picking the last node's output only
    - B) Dropping all results
    - C) Merging their state updates into the shared state`                        '[Correct]'
    - D) Running them again serially

32. Besides reuse, sub-graphs give you:
    - A) Free GPU acceleration
    - B) A separate model per sub-graph
    - C) Automatic encryption
    - D) Isolation — the sub-graph's internals stay contained`                        '[Correct]'

33. In a supervisor pattern, the supervisor node:
    - A) Routes the task to the right specialist agent and aggregates the result`                        '[Correct]'
    - B) Runs every agent in parallel always
    - C) Replaces the LLM
    - D) Stores all memory

34. Handing off control between agents in the supervisor pattern is done via:
    - A) HTTP redirects
    - B) State/commands that route to the next agent node`                        '[Correct]'
    - C) New threads
    - D) Database writes

35. When a sub-graph updates a key, the parent sees the change because:
    - A) The sub-graph writes to a file the parent reads
    - B) It doesn't — changes are lost
    - C) The sub-graph's returned state maps back into the parent's state`                        '[Correct]'
    - D) It recompiles the parent

36. A typical fan-out use case:
    - A) Running one tool twice for verification
    - B) Splitting a message list
    - C) Storing memory
    - D) Generating multiple drafts in parallel, then merging/choosing the best`                        '[Correct]'

37. Why validate input inside a sub-graph rather than inline in the main graph?
    - A) Keeps the main flow clean and lets the validator be reused elsewhere`                        '[Correct]'
    - B) LangGraph requires it
    - C) It makes the LLM faster
    - D) It uses less RAM

38. Two parallel nodes both write the SAME key. What happens?
    - A) They merge automatically
    - B) Last write wins (overwrite) unless a reducer is defined`                        '[Correct]'
    - C) The graph crashes
    - D) A copy is kept per node

39. The supervisor/multi-agent approach mainly helps with:
    - A) Reducing the number of tools
    - B) Guaranteeing faster responses always
    - C) Breaking complex tasks into specialised agents`                        '[Correct]'
    - D) Avoiding the need for memory

40. "Message passing" between agents is implemented in this stack by:
    - A) Sending emails between processes
    - B) Writing to a queue server
    - C) Saving to CSV files
    - D) Passing messages through the shared graph state`                        '[Correct]'

## 5. Human-in-the-Loop

41. `interrupt()` inside a node:
    - A) Pauses the graph and returns control to the caller until resumed`                        '[Correct]'
    - B) Stops the process
    - C) Skips the node
    - D) Saves a checkpoint only

42. The value you pass to `Command(resume=...)` becomes:
    - A) A system message
    - B) The return value of `interrupt()` in that node`                        '[Correct]'
    - C) The new temperature
    - D) A tool result

43. Where should an approval gate sit in the flow?
    - A) After every single LLM call
    - B) Only at the very end of the graph
    - C) Before irreversible/high-impact tool execution`                        '[Correct]'
    - D) It never applies to tools

44. "HITL needs a web UI to work." Is that true?
    - A) Yes, always
    - B) Only for the capstone`                        '[Correct]'
    - C) Only for MCP
    - D) No — HITL is a control-flow pattern; the "human" input can come from code

45. After the human approves, graph execution:
    - A) Resumes from the interrupt checkpoint with the resume value`                        '[Correct]'
    - B) Restarts from START
    - C) Loses the thread state
    - D) Switches to a new thread

46. The most sensible thing to gate with HITL:
    - A) Every weather lookup
    - B) Sending an email or executing a payment`                        '[Correct]'
    - C) Token counting
    - D) Model selection

47. If a human doesn't respond to an interrupt for a while:
    - A) The thread is auto-deleted
    - B) The agent retrains
    - C) State is checkpointed; you can resume the same thread later`                        '[Correct]'
    - D) The tool runs anyway

48. Recording who approved/rejected what is called an:
    - A) Index
    - B) Embedding
    - C) Overlap
    - D) Audit trail`                        '[Correct]'

49. The approve/reject decision in the guardrails HITL is made by:
    - A) A human review node acting on the human's response`                        '[Correct]'
    - B) The LLM by itself
    - C) The ToolNode
    - D) Random choice

50. "Graceful degradation" when the human rejects means:
    - A) The agent crashes with an error
    - B) The agent proceeds without the action and explains, or proposes an alternative`                        '[Correct]'
    - C) The agent retries forever
    - D) The agent ignores the rejection

## 6. MCP — Model Context Protocol

51. MCP's purpose is to give agents:
    - A) A bigger context window
    - B) Access to a GPU
    - C) A standard way to expose/use external tools, resources, and prompts`                        '[Correct]'
    - D) A training dataset

52. `@mcp.prompt` registers:
    - A) A tool the client can call
    - B) A data resource
    - C) A vector index
    - D) A reusable prompt template clients can fetch`                        '[Correct]'

53. For a streamable_http MCP server, the client connects to:
    - A) The server's URL, e.g. `http://localhost:8000/mcp``                        '[Correct]'
    - B) A file path
    - C) A WebSocket endpoint
    - D) The server process ID

54. Which transport needs a separate server process already listening?
    - A) stdio
    - B) streamable_http`                        '[Correct]'
    - C) Neither transport
    - D) Both always spawn the server themselves

55. Tavily's MCP server is best described as:
    - A) A local stdio server you run yourself
    - B) A Docker container in the repo
    - C) A hosted remote server reached over HTTPS with your API key`                        '[Correct]'
    - D) A LangChain built-in tool

56. In the shopping capstone, the agent obtains its tools by:
    - A) Importing them from a module
    - B) Reading a JSON config file
    - C) Asking the user to type them
    - D) Calling `MultiServerMCPClient.get_tools()` on the books server`                        '[Correct]'

57. The books MCP server exposes price lookup through:
    - A) MCP tools plus a resource like `book://{book_id}``                        '[Correct]'
    - B) A SQL table only
    - C) A REST API only
    - D) A CSV file

58. You would choose stdio transport when:
    - A) The client runs on a different machine
    - B) The server is a local subprocess of the same script`                        '[Correct]'
    - C) You need a public URL
    - D) You are connecting to a hosted provider

59. A "connection refused" when connecting to localhost:8000/mcp usually means:
    - A) No internet access
    - B) Wrong LLM model pulled
    - C) The MCP server was not started / is not listening                        '[Correct]'
    - D) The OPENAI key is missing

60. `await client.call_tool("greet", {...})` returns:
    - A) The tool's raw schema
    - B) Nothing — call_tool only fires and forgets                        '[Correct]'
    - C) The server's full log
    - D) The tool's result content

61. An MCP "resource" is:
    - A) Content addressable by a URI (e.g., `book://1`)                        '[Correct]'
    - B) A tool definition
    - C) A prompt template
    - D) A checkpoint

62. The MCP transports used in this training are:
    - A) WebSocket and gRPC
    - B) stdio and streamable_http                        '[Correct]'
    - C) FTP and TCP
    - D) SMTP and HTTPS

63. Which component of the capstone is the MCP server?
    - A) `agent_shopping.py`
    - B) `agentic_chatbot.py`
    - C) `mcp_shopping_server.py`
    - D) All three equally                        '[Correct]'

64. MCP tools differ from ordinary `@tool` functions because they are:
    - A) Defined directly in the agent code
    - B) Always local-only
    - C) Compiled at import time
    - D) Fetched from the MCP server at runtime via `get_tools()`                        '[Correct]'

65. What is needed to run the Tavily MCP client?
    - A) `TAVILY_API_KEY`                        '[Correct]'
    - B) An OpenAI key
    - C) The local Ollama model
    - D) A Postgres connection

## 7. RAG — Retrieval-Augmented Generation

66. Why split documents into chunks before embedding?
    - A) To remove stopwords
    - B) Embedding whole docs is expensive and retrieval becomes imprecise                        '[Correct]'
    - C) To create smaller PDFs
    - D) To enable multi-user access

67. If a chunk is too large, the typical problem is:
    - A) Retrieval becomes faster
    - B) Nothing changes
    - C) Embedding quality and retrieval relevance drop, and context-window pressure grows                        '[Correct]'
    - D) The splitter crashes

68. The retriever's output is used by the LLM as:
    - A) New tools
    - B) Training data
    - C) A checkpointer
    - D) Context in the prompt when generating the answer                        '[Correct]'

69. Retrieval beats stuffing the entire document into the prompt because:
    - A) The model only gets the focused, relevant context                        '[Correct]'
    - B) The model gets more tokens
    - C) It requires no embeddings
    - D) It always gives the exact same answer

70. Why does MultiQueryRetriever improve recall?
    - A) It embeds the whole corpus again
    - B) Different question phrasings retrieve different relevant chunks                        '[Correct]'
    - C) It doubles the chunk size
    - D) It uses a bigger model

71. HyDE helps by:
    - A) Encrypting the documents
    - B) Making embeddings smaller
    - C) Generating a hypothetical passage that bridges the query/document semantic gap                        '[Correct]'
    - D) Skipping retrieval entirely

72. Similar texts end up close together in embedding space, which is why:
    - A) We can compress them
    - B) We can delete duplicates                        '[Correct]'
    - C) We use a database
    - D) Vector similarity is a reliable retrieval signal

73. A similarity search over the vector store returns:
    - A) The chunks most similar to the query embedding
    - B) All documents
    - C) Random chunks
    - D) Tool outputs                        '[Correct]'

74. RAG reduces hallucination mainly by:
    - A) Using a larger context window
    - B) Grounding the answer in retrieved evidence                        '[Correct]'
    - C) Fine-tuning the model
    - D) Adding a system prompt

75. Retrieval keeps returning irrelevant chunks. The best first fix is:
    - A) Increase the temperature
    - B) Add more tools
    - C) Improve chunking/overlap, embeddings, or use multi-query retrieval                        '[Correct]'
    - D) Switch to a different OS

## 8. Guardrails & Security

76. Deterministic (regex/rule) guardrails are usually applied first because:
    - A) They are perfectly accurate
    - B) They need GPUs
    - C) They handle nuance well
    - D) They are cheap and fast                        '[Correct]'

77. Model-based guardrails are preferred when:
    - A) The decision needs semantic understanding (is this content unsafe?)                        '[Correct]', Need much better understanding
    - B) You need exact regex matches
    - C) You must minimise cost
    - D) You have no LLM available

78. An output guardrail runs:
    - A) Before the LLM sees the input
    - B) After model generation, before the response reaches the user                        '[Correct]'
    - C) During training
    - D) Never in this training

79. Redacting the email before the model means:
    - A) The model gets it via a tool instead
    - B) It is saved to a log
    - C) The raw PII never reaches the LLM call                        '[Correct]'
    - D) The whole message is blocked

80. Filtering a request like "how do I hack..." at input time is:
    - A) Output filtering
    - B) HITL
    - C) RAG retrieval
    - D) Input/harmful-content filtering                        '[Correct]'

81. Middleware in `create_agent` wraps:
    - A) Model and tool calls — input flows through the layers before/after each                        '[Correct]'
    - B) Only the chat UI
    - C) The vector store
    - D) The database

82. Layered guardrails (deterministic + model-based + HITL) are used because:
    - A) Each layer is faster
    - B) No single check is perfect — defence in depth                        '[Correct]'
    - C) Fewer tools are needed
    - D) The prompt can be shorter

83. A guardrail false positive (safe input blocked) means:
    - A) The system is perfect
    - B) Ignore it — safety always wins
    - C) User experience suffers — tune thresholds carefully                        '[Correct]'
    - D) The guardrail is broken permanently

84. Guardrails can also validate tool-call arguments in order to:
    - A) Speed up the tools
    - B) Cache the results
    - C) Reduce token usage
    - D) Prevent risky or injected tool invocations                        '[Correct]'

85. Prompt injection ("ignore your instructions") is best defended by:
    - A) Treating user input as untrusted data and filtering/validating it before it influences tool flows                        '[Correct]'
    - B) Never responding to users
    - C) Removing the system prompt
    - D) Using a bigger model

## 9. Environment & App Wiring

86. A notebook fails with a localhost connection error. The first suspect is:
    - A) Gradio is not installed
    - B) Ollama is not running / the model is not pulled                        '[Correct]'
    - C) The Python version
    - D) No internet

87. Where should your cloud API keys live in this repo?
    - A) Hardcoded in the notebooks
    - B) In requirements.txt
    - C) In a repo-root `.env` file loaded via python-dotenv                        '[Correct]'
    - D) In the system prompt

88. Which of these needs cloud API keys in this repo?
    - A) All notebooks
    - B) The Ollama notebooks
    - C) None
    - D) The OpenAI RAG notebooks and the Tavily MCP clients                        '[Correct]'

89. The Gradio UI talks to the shopping agent by:
    - A) Importing `get_shopping_agent` from `agent_shopping` and invoking it                        '[Correct]'
    - B) HTTP calls to port 8000
    - C) A stdio subprocess
    - D) It doesn't talk to the agent

90. Corporate SSL errors when installing/running typically mean:
    - A) Python is outdated
    - B) The corporate proxy CA must be trusted (certifi/pyOpenSSL/python-certifi-win32)                        '[Correct]'
    - C) Use HTTP instead of HTTPS
    - D) Reinstall Windows

---

## Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1  | A  | 19 | C  | 37 | A  | 55 | C  | 73 | A  |
| 2  | B  | 20 | D  | 38 | B  | 56 | D  | 74 | B  |
| 3  | C  | 21 | A  | 39 | C  | 57 | A  | 75 | C  |
| 4  | D  | 22 | B  | 40 | D  | 58 | B  | 76 | D  |
| 5  | A  | 23 | C  | 41 | A  | 59 | C  | 77 | A  |
| 6  | B  | 24 | D  | 42 | B  | 60 | D  | 78 | B  |
| 7  | C  | 25 | A  | 43 | C  | 61 | A  | 79 | C  |
| 8  | D  | 26 | B  | 44 | D  | 62 | B  | 80 | D  |
| 9  | A  | 27 | C  | 45 | A  | 63 | C  | 81 | A  |
| 10 | B  | 28 | D  | 46 | B  | 64 | D  | 82 | B  |
| 11 | C  | 29 | A  | 47 | C  | 65 | A  | 83 | C  |
| 12 | D  | 30 | B  | 48 | D  | 66 | B  | 84 | D  |
| 13 | A  | 31 | C  | 49 | A  | 67 | C  | 85 | A  |
| 14 | B  | 32 | D  | 50 | B  | 68 | D  | 86 | B  |
| 15 | C  | 33 | A  | 51 | C  | 69 | A  | 87 | C  |
| 16 | D  | 34 | B  | 52 | D  | 70 | B  | 88 | D  |
| 17 | A  | 35 | C  | 53 | A  | 71 | C  | 89 | A  |
| 18 | B  | 36 | D  | 54 | B  | 72 | D  | 90 | B  |
