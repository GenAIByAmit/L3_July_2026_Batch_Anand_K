# Zensar L3 AI — Practice Objective Questions

Practice MCQs for the internal Zensar L3 test, mapped to the taught material (day-wise notebooks, MCP capstone, guardrails, RAG). Answer key at the bottom.

---

## 1. LLM Fundamentals & Tool Calling (Days 01–02)

1. What is the default LLM used across this training's notebooks?
   - A) `ChatOpenAI(model="gpt-4o")`
   - B) `HuggingFacePipeline(model="gpt-oss:120b-cloud")`                   
   - C) `ChatOllama(model="gpt-oss:120b-cloud")`                        '[Correct]'
   - D) `ChatGroq(model="llama3-8b-8192")`

2. Where does the `gpt-oss:120b-cloud` model run in this training?
   - A) On a local Ollama server                        '[Correct]'
   - B) On OpenAI's API
   - C) On Zensar's cloud API
   - D) Inside the notebook kernel only

3. What is the minimum configuration required for `create_agent`?
   - A) `model` only
   - B) `tools` and `checkpointer`
   - C) `model`, `prompt`, `retriever`
   - D) `model`, `tools`, and `system_prompt`                        '[Correct]'

4. In the `@tool` decorator pattern, what defines the tool's name and arguments?
   - A) The decorator parameters
   - B) The function name and its typed parameters                        '[Correct]'
   - C) The `create_agent` call
   - D) The system prompt

5. Why is a descriptive docstring important on a `@tool` function?
   - A) It is returned to the user verbatim
   - B) It is used as the tool's name
   - C) It is passed to the LLM so it knows when and how to call the tool                        '[Correct]'
   - D) It is required by Python to compile

6. How do you give an LLM the ability to call tools in LangChain?
   - A) `llm.bind_tools(tools)`
   - B) `llm.invoke(tools=[...])`                        '[Correct]'
   - C) `tools.bind(llm)`
   - D) `llm.attach(tools)`

7. Which package provides built-in tools like `DuckDuckGoSearchResults` and `WikipediaQueryRun`?
   - A) `langchain_mcp_adapters`
   - B) `langchain_ollama`
   - C) `langchain_core`
   - D) `langchain_community`                        '[Correct]'

8. What does `WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)` control?
   - A) The model used for summarization
   - B) The number of results and maximum characters per result                        '[Correct]'
   - C) The search engine to query
   - D) The embedding model used

9. Which API key is required by the Tavily search tool?
   - A) `OPENAI_API_KEY`
   - B) `GROQ_API_KEY`
   - C) `TAVILY_API_KEY`                        '[Correct]'
   - D) `HF_TOKEN`

10. In `agent.invoke({"messages": [{"role": "user", "content": "..."}]})`, what is the state key that all agents expect?
    - A) `"input"`
    - B) `"messages"`
    - C) `"query"`
    - D) `"chat_history"`                        '[Correct]'

## 2. Agent Memory (Days 03–04)

11. In Day-3 (`03_agent_memory.ipynb`), short-term memory is implemented with:
    - A) A Python list the developer manages manually
    - B) A vector database
    - C) `MemorySaver` checkpointing via `thread_id`                        ,'[Correct]', '[Feedback: not good question]'
    - D) Redis

12. What is the correct way to identify a conversation thread for checkpointed memory?
    - A) `{"session_id": "tom"}`
    - B) `{"configurable": {"thread_id": "tom"}}`                        '[Correct]'
    - C) `{"thread": "tom"}`
    - D) `{"user": "tom"}`

13. "Memory is not in the agent, it's in how we call it" means:
    - A) The agent must be recreated per user
    - B) The system prompt must be regenerated each call
    - C) Memory only works with cloud models
    - D) The same agent instance can be reused across users via different `thread_id`s                        '[Correct]'

14. `MemorySaver.get(config)` returns:
    - A) The full conversation state/messages for that thread                        '[Correct]'
    - B) Only the last user message
    - C) The tool definitions
    - D) The model response only

15. What is the difference between `MemorySaver` (checkpointer) and `InMemoryStore`?
    - A) Short-term per-thread checkpointing vs. long-term cross-session storage keyed by user                        '[Correct]'
    - B) One is for OpenAI, the other for Ollama
    - C) They are identical aliases
    - D) One stores tools, the other stores messages

16. Which store is used for long-term memory that persists across sessions and "works on user_id"?
    - A) `MemorySaver`                        '[Correct]'
    - B) `ChatMessageHistory`
    - C) `InMemoryStore`
    - D) `MemoryStore`

17. How can an agent write its own long-term memory at runtime?
    - A) By using memory tools that call `get_store` / `get_config` from `langgraph.config`
    - B) By returning `{"memory": ...}` from a node
    - C) By saving to the `thread_id`                        '[Correct]'
    - D) By appending to the system prompt

18. What does `langgraph.store.sqlite.SqliteStore` provide?
    - A) In-memory-only persistence
    - B) Persistent long-term memory backed by a SQLite database                        '[Correct]'
    - C) A replacement for the checkpointer
    - D) Memory for tool outputs only

19. When the same agent is invoked with a different `thread_id`, what happens to the conversation context?
    - A) It is shared across all threads
    - B) Each thread gets its own isolated conversation state                        '[Correct]'
    - C) The new thread overrides the old one
    - D) The agent errors out

20. Which is NOT a legitimate way to implement memory discussed in the training?
    - A) Manual conversation list managed by the developer
    - B) `MemorySaver` checkpointing
    - C) Storing secrets in the system prompt for reuse                        '[Correct]'
    - D) SQLite-backed long-term store

## 3. LangGraph Fundamentals (Day 05)

21. Which class builds a graph in LangGraph?
    - A) `Graph`
    - B) `AgentGraph`                        '[Correct]'
    - C) `Workflow`
    - D) `StateGraph`

22. What is used to define the shape of the state passed between graph nodes?
    - A) A dataclass
    - B) A `TypedDict`
    - C) A Pydantic `Settings` object
    - D) A JSON schema file                        '[Correct]'

23. In `StateGraph(AgentState)`, what do nodes typically return?
    - A) A full replacement of state                        '[Correct]'
    - B) The final answer only
    - C) A dictionary of partial updates merged into the state
    - D) An AIMessage list

24. Which edge functions connect nodes in LangGraph?
    - A) `add_node` and `add_state`
    - B) `add_edge`, `add_conditional_edges`, plus `START`/`END`                        '[Correct]'
    - C) `connect` and `link`
    - D) `append` and `merge`

25. What is the role of `ToolNode` from `langgraph.prebuilt`?
    - A) It executes tool calls returned by the model in a graph                        '[Correct]'
    - B) It calls the LLM
    - C) It stores conversation history
    - D) It validates tool arguments

26. A conditional edge that routes to tools is typically based on:
    - A) Whether the user typed "tool"
    - B) The length of the user message
    - C) Whether the last AI message contains `tool_calls`                        '[Correct]'
    - D) The `thread_id` value

27. What does `graph.stream({"messages": [...]}, {"configurable": {"thread_id": ...}})` return?
    - A) A stream of intermediate events/state as the graph executes                        '[Correct]'
    - B) Only the final state
    - C) The model's token stream
    - D) A list of all threads

28. Which package provides `create_agent` used in the notebooks and the capstone?
    - A) `langchain_ollama`
    - B) `langchain.agents`                        '[Correct]' not good queestion
    - C) `langgraph.prebuilt`
    - D) `fastmcp`

29. In the ReAct-style graph, the assistant node and ToolNode form a loop. What terminates the loop?
    - A) A maximum token count
    - B) A conditional edge routing to END when no more tool calls are requested                        '[Correct]'
    - C) The user pressing stop
    - D) A fixed iteration of 3

30. What is the purpose of `llm.bind_tools(TOOLS)` before building the tool graph?
    - A) It tells the model which tools exist so it can emit structured tool calls                        '[Correct]'
    - B) It validates the tools' syntax
    - C) It compiles the tools into native code
    - D) It trains the model on the tools

## 4. Parallel Nodes, Sub-Graphs, & Multi-Agent (Days 07–08)

31. The "fan-in fan-out" pattern means:
    - A) One node calls the LLM repeatedly
    - B) Work fans out to multiple parallel nodes, then their results are combined                        '[Correct]'
    - C) The graph duplicates itself
    - D) Messages are split between users

32. When can two nodes in a LangGraph run in parallel?
    - A) Always, regardless of dependencies                        '[Correct]'
    - B) Only when they use different models
    - C) When both read from the state and update disjoint keys (no data dependency)
    - D) Only when the user requests it

33. What is a sub-graph in LangGraph?
    - A) A graph within the main graph, invoked as a node                        '[Correct]'
    - B) A smaller version of the model
    - C) A graph that has no START
    - D) A single node with multiple edges

34. In the Day-8 example, the sub-graph was used for:
    - A) Summarizing long text
    - B) Input validation (e.g., `check_length` on the topic)                           '[Correct]'- not good question why becuase expecting questions based on concept and not day specific
    - C) Storing chat history
    - D) Calling external APIs

35. How does a parent graph invoke a sub-graph?
    - A) Through `subgraph.run()`
    - B) By adding the sub-graph as a node, passing it state                        '[Correct]'
    - C) By importing it inside the system prompt
    - D) Sub-graphs cannot be invoked from another graph

36. Which state key pattern is used to append messages across nodes (vs. overwrite)?
    - A) `Annotated[list, operator.add]`
    - B) A plain `TypedDict` list
    - C) `message_key: str`                        '[Correct]'
    - D) `list[str]` without annotation

37. In a supervisor/multi-agent setup, who decides which agent handles the task?
    - A) The user directly
    - B) A routing LLM node                        '[Correct]'
    - C) The first tool called
    - D) Random selection

38. What problem do parallel nodes solve in agent workflows?
    - A) Reducing latency by running independent steps concurrently                        '[Correct]'
    - B) Reducing LLM temperature
    - C) Reducing token usage of the system prompt
    - D) Making the graph stateful

39. Sub-graphs are useful for:
    - A) Hiding API keys
    - B) Running the LLM offline
    - C) Reusing a validated sub-workflow across multiple graphs                        '[Correct]'
    - D) Storing embeddings

40. `StateGraph(BlogState).add_node(...)` for fan-in/fan-out might define:
    - A) Two independent content-writing nodes that both update the final state                        '[Correct]'
    - B) A single node writing the whole blog
    - C) A cycle with no end
    - D) A checkpointer that writes to disk

## 5. Human-in-the-Loop (Day 07)

41. What does `interrupt()` do in a LangGraph HITL node?
    - A) Stops the LLM mid-response
    - B) Pauses graph execution and returns control to the human                        '[Correct]'
    - C) Restarts the graph
    - D) Sends an email

42. In the HITL example, the "Human Review Node" is responsible for:
    - A) Reviewing and approving/rejecting a sensitive tool call (e.g., sending an email)                        '[Correct]'
    - B) Summarizing the chat
    - C) Cleaning tool outputs
    - D) Selecting the thread_id

43. How is the graph resumed after a human approves an interrupted action?
    - A) By re-running the whole graph from START
    - B) By invoking with `Command(resume=...)` using the same `thread_id`                        '[Correct]'
    - C) By calling `graph.stop()`
    - D) By deleting the thread

44. Why is the `thread_id` essential for HITL?
    - A) It defines the model
    - B) It is used for billing
    - C) It lets the graph pause and resume at the exact checkpoint                        '[Correct]'
    - D) It decides routing

45. Which is a valid human-in-the-loop pattern shown in the training?
    - A) Approve a sensitive tool call before it executes                        '[Correct]'
    - B) Reject and let the LLM recover with feedback
    - C) Both approve and reject flows are shown
    - D) Neither; HITL is only about UI

46. HITL (Human-in-the-Loop) is most important when:
    - A) The user is not online
    - B) The graph is very fast
    - C) The model is small
    - D) Actions have high cost/risk and need human approval                        '[Correct]'

47. `Command` in LangGraph is used to:
    - A) Return control with a resume value and/or continue to specific nodes                        '[Correct]'
    - B) Set the temperature
    - C) Compile the graph
    - D) Serialize the state

48. When the human rejects, the graph can:
    - A) Crash permanently
    - B) Provide feedback to the model so it can answer without performing the action                        '[Correct]'
    - C) Delete the thread
    - D) Switch models

49. In the guardrails notebook's HITL example, which tool pauses for approval?
    - A) `search_tool`
    - B) `send_email_tool`
    - C) `customer_lookup`                        '[Correct]', this question is not good
    - D) `get_weather`

50. Which config key resumes a paused thread?
    - A) A new `thread_id`
    - B) `{"resume": true}`                        '[Correct]'
    - C) `{"configurable": {"thread_id": "test_001"}}` (same thread, with `Command`)
    - D) `{"checkpoint": 1}`

## 6. MCP — Model Context Protocol (Day 09 + capstone)

51. MCP stands for:
    - A) Multi Cloud Platform
    - B) Model Context Protocol                        '[Correct]'
    - C) Model Call Process
    - D) Message Control Protocol

52. Which decorator registers a tool in FastMCP?
    - A) `@mcp.tool`                        '[Correct]'
    - B) `@mcp.function`
    - C) `@mcp.callable`
    - D) `@tool.register`

53. In FastMCP, resources are defined with:
    - A) `@mcp.data`
    - B) `@mcp.store`
    - C) `@mcp.file`
    - D) `@mcp.resource("book://{book_id}")`                        '[Correct]'

54. What are the three core MCP primitives used in the training?
    - A) tools, resources, prompts                        '[Correct]'
    - B) tools, models, agents
    - C) tools, memory, storage
    - D) endpoints, schemas, auth

55. What is the default transport when you call `mcp.run()` without arguments?
    - A) HTTP                        '[Correct]'
    - B) stdio
    - C) WebSocket
    - D) TCP

56. In `09_local_shttp_mcp_server.py`, `mcp.run(transport="http", port=8000)` uses which HTTP-based protocol?
    - A) Server-Sent Events only
    - B) streamable HTTP (default shttp)                        '[Correct]'
    - C) gRPC
    - D) FTP

57. Which command runs the shopping MCP server on port 8000?
    - A) `python agent_shopping.py`
    - B) `python mcp_shopping_server.py`                        '[Correct]'
    - C) `python agentic_chatbot.py`
    - D) `python 09_local_stdio_mcp_client.py`

58. The LangGraph shopping agent connects to the MCP server using:
    - A) `http://localhost:8000/mcp` with `transport="streamable_http"`                        '[Correct]'
    - B) A stdio subprocess
    - C) `http://localhost:7860/mcp`
    - D) `https://mcp.tavily.com/mcp`

59. `MultiServerMCPClient` comes from:
    - A) `fastmcp`
    - B) `langchain_community`
    - C) `langchain_mcp_adapters.client`                        '[Correct]'
    - D) `tavily-python`

60. The Gradio chatbot UI in the capstone runs on:
    - A) Port 8000
    - B) Port 5000
    - C) Port 8080
    - D) Port 7860                        '[Correct]', this is not good question

61. In `fastmcp.Client`, calling a remote tool looks like:
    - A) `await client.call_tool("greet", {"name": "Tom"})`                        '[Correct]'
    - B) `client.invoke("greet", {...})`
    - C) `client.run("greet")`
    - D) `client.send("greet")`

62. Why must `mcp_shopping_server.py` be started BEFORE `agent_shopping.py`?
    - A) It sets environment variables
    - B) The agent fails to connect if the server is not listening on port 8000                        '[Correct]'
    - C) The server must train first
    - D) It creates the Gradio port

63. `client.list_tools()` returns:
    - A) The list of tools exposed by the MCP server                        '[Correct]'
    - B) The list of installed Python packages
    - C) The conversation history
    - D) The tool outputs

64. A stdio MCP client connects by passing:
    - A) A URL
    - B) The path to the server script, e.g., `Client("09_local_stdio_mcp_server.py")`                        '[Correct]'
    - C) A port number only
    - D) An API key

65. Tavily's hosted MCP endpoint requires the API key to be passed:
    - A) In the system prompt
    - B) As a query parameter `?tavilyApiKey=...`
    - C) Via a config file                        '[Correct]'
    - D) It is free and needs no key

## 7. RAG — Retrieval-Augmented Generation (Day 10)

66. `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)` does what?
    - A) Splits documents into 50 chunks of 500 chars
    - B) Splits documents into 500-char chunks with 50-char overlap between chunks                        '[Correct]'
    - C) Removes 500 chars from each document
    - D) Combines documents into a single 500-char chunk

67. Why is `chunk_overlap` used?
    - A) To reduce storage size
    - B) To speed up embedding
    - C) To avoid losing context at chunk boundaries during retrieval                        '[Correct]'
    - D) To deduplicate chunks

68. Which class builds a FAISS vector store in the training?
    - A) `FAISS.from_documents(docs, embeddings)`
    - B) `FAISS.store(docs)`
    - C) `VectorStore.create(docs)`
    - D) `FAISS.load(docs)`                        '[Correct]'

69. What does `MultiQueryRetriever` do?
    - A) Retrieves documents from multiple databases
    - B) Uses the LLM to generate multiple query variations to improve retrieval recall                        '[Correct]'
    - C) Runs multiple models in parallel
    - D) Combines chunking strategies

70. In the HyDE (Hypothetical Document Embeddings) approach:
    - A) Documents are encrypted before embedding
    - B) The user writes fake documents
    - C) Embeddings are compressed to 8-bit
    - D) A hypothetical passage that would answer the question is generated, then embedded and retrieved against                        '[Correct]'

71. Which embedding model does the OpenAI-based RAG notebook use by default?
    - A) `OpenAIEmbeddings()`                        '[Correct]'
    - B) `HuggingFaceEmbeddings`
    - C) `nomic-ai/nomic-embed-text-v1.5`
    - D) Ollama embeddings

72. Which embeddings + vector store combo does the HyDE notebook use?
    - A) OpenAIEmbeddings + FAISS
    - B) GPT embeddings + SQLite
    - C) HuggingFaceEmbeddings + Chroma                        '[Correct]'
    - D) Ollama + Redis

73. `RetrievalQA.from_chain_type(..., chain_type="stuff")`:
    - A) Returns the retrieved docs only
    - B) Stuffs all retrieved docs into the prompt as context                        '[Correct]'
    - C) Loads docs into memory
    - D) Runs a map-reduce pass

74. A key benefit of multi-query retrieval and HyDE is:
    - A) Faster model inference
    - B) Cheaper embeddings
    - C) Better retrieval quality/recall for ambiguous queries                        '[Correct]'
    - D) Smaller documents

75. The general RAG pipeline order is:
    - A) Embed → retrieve → split → generate
    - B) Load → split → embed → index/store → retrieve → generate
    - C) Split → generate → embed → retrieve                        '[Correct]'
    - D) Retrieve → load → generate → split

## 8. Guardrails & Security

76. The two approaches to guardrails illustrated in `guardrails.ipynb` are:
    - A) Deterministic (rule-based) and Model-based                        '[Correct]'
    - B) Cloud and on-premise
    - C) Regex and encryption
    - D) Sync and async

77. Which of these is a deterministic guardrail technique?
    - A) An LLM judging output safety
    - B) Regex-based PII/email redaction                        '[Correct]'
    - C) A second model for moderation
    - D) Semantic similarity scoring

78. A model-based guardrail typically:
    - A) Uses regex rules only
    - B) Blocks all user input
    - C) Asks an LLM to return SAFE/UNSAFE (or similar) verdicts on text                        '[Correct]'
    - D) Removes stopwords

79. Which is an example of prompt injection defense covered in the training?
    - A) Adding API keys to the prompt
    - B) Filtering/redacting inputs and validating tool calls                        '[Correct]'
    - C) Increasing temperature
    - D) Using a larger context window

80. What does PII redaction do in the guardrail examples?
    - A) It removes personally identifiable information (e.g., emails) from user input before it reaches the model                        '[Correct]'
    - B) It deletes the conversation
    - C) It anonymizes the thread_id
    - D) It encrypts the whole prompt

81. The `AgentMiddleware` class in the guardrails notebook is used to:
    - A) Compile the graph
    - B) Add layers that filter inputs/outputs around model and tool calls                        '[Correct]'
    - C) Connect to the MCP server
    - D) Build the vector store

82. In a layered guardrail stack, the recommended order is:
    - A) Cheap deterministic checks first, model-based checks second                        '[Correct]'
    - B) Model-based checks first, deterministic second
    - C) Only model-based checks
    - D) Order does not matter

83. Blocking an API key from appearing in prompts is an example of:
    - A) Output safety evaluation                        '[Correct]'
    - B) Input filtering guardrail
    - C) RAG retrieval
    - D) Memory management

84. The healthcare filter example blocks:
    - A) All medical questions
    - B) Non-medical/harmful requests and redacts PII                        '[Correct]'
    - C) Only appointment bookings
    - D) Only emails

85. Which of the following is a middleware layer demonstrated in the full stack?
    - A) PII redaction middleware
    - B) Output safety middleware
    - C) HITL approval for sensitive tools
    - D) All of the above                        '[Correct]', not good question

## 9. Environment & App Wiring (repo-specific)

86. What must be running locally for most notebooks to work?
    - A) Docker with Postgres
    - B) Ollama with the `gpt-oss:120b-cloud` model pulled                        '[Correct]'
    - C) An NGINX reverse proxy
    - D) The Tavily CLI

87. Cloud-API keys (OpenAI, Tavily) are read from:
    - A) A repo-root `.env` file via python-dotenv `find_dotenv()`                        '[Correct]'
    - B) Hardcoded strings in the notebooks
    - C) The Windows registry
    - D) A requirements.txt entry

88. The `requirements.txt` includes `python-certifi-win32` because:
    - A) It accelerates Ollama
    - B) It is required for LangGraph                        '[Correct]'
    - C) SSL errors on corporate networks usually need the corporate proxy CA trusted
    - D) It is the embedding backend

89. Which statement about running the capstone is correct?
    - A) `agentic_chatbot.py` must start before `mcp_shopping_server.py`
    - B) `mcp_shopping_server.py` starts first, then `agent_shopping.py`, then `agentic_chatbot.py`                        '[Correct]'
    - C) All three can run in any order
    - D) Only `agentic_chatbot.py` needs to run

90. `agent_shopping.py` has a known gotcha:
    - A) It requires a GPU
    - B) It calls `asyncio.run()` at module level
    - C) It uses no tools                        '[Correct]'
    - D) It connects to a database

---

## Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1  | C  | 19 | B  | 37 | B  | 55 | B  | 73 | B  |
| 2  | A  | 20 | C  | 38 | A  | 56 | B  | 74 | C  |
| 3  | D  | 21 | D  | 39 | C  | 57 | B  | 75 | B  |
| 4  | B  | 22 | B  | 40 | A  | 58 | A  | 76 | A  |
| 5  | C  | 23 | C  | 41 | B  | 59 | C  | 77 | B  |
| 6  | A  | 24 | B  | 42 | A  | 60 | D  | 78 | C  |
| 7  | D  | 25 | A  | 43 | B  | 61 | A  | 79 | B  |
| 8  | B  | 26 | C  | 44 | C  | 62 | B  | 80 | A  |
| 9  | C  | 27 | A  | 45 | C  | 63 | A  | 81 | B  |
| 10 | B  | 28 | B  | 46 | D  | 64 | B  | 82 | A  |
| 11 | C  | 29 | B  | 47 | A  | 65 | B  | 83 | B  |
| 12 | B  | 30 | A  | 48 | B  | 66 | B  | 84 | B  |
| 13 | D  | 31 | B  | 49 | B  | 67 | C  | 85 | D  |
| 14 | A  | 32 | C  | 50 | C  | 68 | A  | 86 | B  |
| 15 | A  | 33 | A  | 51 | B  | 69 | B  | 87 | A  |
| 16 | C  | 34 | B  | 52 | A  | 70 | D  | 88 | C  |
| 17 | A  | 35 | B  | 53 | D  | 71 | A  | 89 | B  |
| 18 | B  | 36 | A  | 54 | A  | 72 | C  | 90 | B  |
