import asyncio
from fastmcp import Client
from tavily import TavilyClient
import os
from dotenv import load_dotenv, find_dotenv
from google.colab import userdata

tavilyApiKey = userdata.get('TAVILY_API_KEY')

tavily_client = Client(f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavilyApiKey}")

async def call_tavily_mcp_server(query: str):
    async with tavily_client:
        result = await tavily_client.call_tool("search", {"query": query})
        print(result)

async def call_tavily_mcp_server(query: str):
    async with tavily_client:
        result = await tavily_client.call_tool("tavily_search", {"query": query})
        print(result)

async def list_tools():
    async with tavily_client:
        tools = await tavily_client.list_tools()
        print(tools)
        #print(len(tools))
        for tool in tools:
            print(tool)

#await list_tools()
await call_tavily_mcp_server("What is Generative AI?")
#await call_tavily_mcp_server("What is the capital of France?")