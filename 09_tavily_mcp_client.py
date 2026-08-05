import asyncio
from fastmcp import Client
from dotenv import load_dotenv
load_dotenv()
import os

client = Client(
    f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('TAVILY_API_KEY')}"
)

async def call_tavily_mcp_server():
    
    async with client:
        #result = await client.call_tool("greet", {"name": name})
        tools = await client.list_tools()

        print("Available tools:")
        print("-" * 40)

        for tool in tools:
            print(tool)


asyncio.run(call_tavily_mcp_server())
