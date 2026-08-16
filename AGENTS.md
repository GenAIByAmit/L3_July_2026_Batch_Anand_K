# AGENTS.md

Zensar AI L3 training repo: day-wise LangChain / LangGraph / MCP / RAG notebooks (`01`–`10`, `guardrails.ipynb`) plus a `shopping_agentic_app` capstone. Teaching demos — don't restructure them; edit only when asked.

## LLM setup
- Default model everywhere is local Ollama: `ChatOllama(model="gpt-oss:120b-cloud")`. Ollama must be running locally with that model pulled, or every notebook/script fails with a connection error.
- A few files use cloud APIs instead: RAG notebooks (`10_*`) use OpenAI (`gpt-3.5-turbo`, `OpenAIEmbeddings`); MCP clients use Tavily. Keys are read from a repo-root `.env` via python-dotenv (`find_dotenv()`). Create `.env` with `OPENAI_API_KEY`, `TAVILY_API_KEY`, etc. — it is not committed, and there is no `.gitignore`.

## shopping_agentic_app (capstone)
Run in this order:
1. `python mcp_shopping_server.py` — FastMCP HTTP server, port 8000 (`streamable_http`).
2. `python agent_shopping.py` — LangGraph agent; connects to `http://localhost:8000/mcp`. Gotcha: it calls `asyncio.run()` at module level (lines 55–56).
3. `python agentic_chatbot.py` — Gradio chat UI on port 7860; imports `get_shopping_agent` from `agent_shopping`.

## Verification
- No tests, lint, or CI config. Verify by running the target script/notebook directly.
- No lockfile; install from `requirements.txt`.

## Environment gotchas
- Corporate network: requirements include `certifi` / `pyOpenSSL` / `python-certifi-win32` — SSL errors usually mean the corporate proxy CA needs to be trusted or environment variables set.
- Day-9 files (`09_*.py`) are standalone MCP demos (fastmcp + local stdio/http servers + Tavily client + a Colab variant); several call `asyncio.run()` at module level.
