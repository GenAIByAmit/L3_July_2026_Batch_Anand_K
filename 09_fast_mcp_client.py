import asyncio
from fastmcp import Client
from tavily import TavilyClient
import os
from dotenv import load_dotenv, find_dotenv


env_path = find_dotenv()
if not env_path:
    raise FileNotFoundError(".env file not found.")

load_dotenv(env_path)
tavilyApiKey = os.getenv("TAVILY_API_KEY")
os.environ["TAVILY_API_KEY"] = tavilyApiKey

client = Client("http://localhost:8000/mcp")
tavily_client = Client(f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavilyApiKey}")

async def call_greet(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

async def call_add(x: int, y: int):
    async with client:
        result = await client.call_tool("add", {"a": x, "b": y})
        print(result)

async def call_tavily_mcp_server(query: str):
    async with tavily_client:
        result = await tavily_client.call_tool("tavily_search", {"query": query})
        print(result)

async def list_tools():
    async with tavily_client:
        tools = await tavily_client.list_tools()
        print(tools)

#asyncio.run(call_greet("Ford"))
#asyncio.run(list_tools())
asyncio.run(call_tavily_mcp_server("What is the capital of France?"))
