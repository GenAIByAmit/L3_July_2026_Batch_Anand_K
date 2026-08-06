from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.checkpoint.memory import MemorySaver
import asyncio

# Initialize the Ollama chat model
chat_model = ChatOllama(model="gpt-oss:120b-cloud", temperature=0)

client = MultiServerMCPClient(
    {
        "books": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http"
        }
    }
)

memory = MemorySaver()

async def get_all_tools():
    """
    Returns a list of tools available for the shopping agent.
    """
    tools = await client.get_tools()
    return tools

async def get_resources():
    """
    Returns a list of resources available for the shopping agent.
    """
    resources = await client.get_resources()
    return resources

async def get_shopping_agent():
    tools = await get_all_tools()
    resources = await get_resources()
    print(f"Tools available for the shopping agent: {len(tools)}")
    print(tools)
    # Create an agent with the chat model
    global shopping_agent
    shopping_agent = create_agent(
        model=chat_model,
        tools=tools,
        system_prompt="You are a helpful shopping assistant. You can provide information about books, their prices, and availability. Use the available tools and resources to assist the user effectively.",
        checkpointer=memory
        )

    return shopping_agent

async def call_prompt():
    prompt = await client.get_prompt(server_name="books", prompt_name="get_book_price_prompt", arguments={"book_name": "Panch tantra"})
    print(f"Prompt: {prompt}")

asyncio.run(get_shopping_agent())
asyncio.run(call_prompt())