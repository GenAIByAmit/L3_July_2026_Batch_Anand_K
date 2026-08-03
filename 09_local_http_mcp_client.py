# MCP stdio client
from fastmcp import Client
import asyncio

client = Client("http://localhost:8000/mcp")

async def call_greet(name: str):
    async with client:
        greet_message = await client.call_tool("greet", {"name": name}) #await is a blocking call
        print(greet_message)

if __name__ == "__main__":
    asyncio.run(call_greet("Tom"))
    asyncio.run(call_greet("Jerry"))