from fastmcp import FastMCP
import os
from dotenv import load_dotenv, find_dotenv
from tavily import TavilyClient

env_path = find_dotenv()
if not env_path:
    raise FileNotFoundError(".env file not found.")

load_dotenv(env_path)
tavilyApiKey = os.getenv("TAVILY_API_KEY")
os.environ["TAVILY_API_KEY"] = tavilyApiKey

mcp = FastMCP("Demo 🚀")

isd_codes = [
  {
    "name": "India",
    "dial_code": "+91",
    "code": "IN"
  },
  {
    "name": "Russia",
    "dial_code": "+7",
    "code": "RU"
  },
  {
    "name": "United Kingdom",
    "dial_code": "+44",
    "code": "GB"
  },
  {
    "name": "United States",
    "dial_code": "+1",
    "code": "US"
  }
]

@mcp.resource("isdcodes://{country_code}")
def get_isd_code(country_code: str) -> str:
    """Get the dial code for a given country code."""
    for country in isd_codes:
        if country["code"] == country_code:
            return country["dial_code"]
    return "Country not found."

@mcp.prompt
def capital_city_prompt(country_name: str) -> str:
    """Prompt to get the capital city of a country."""
    return f"What is the capital city of {country_name}?"

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"

@mcp.tool
def search_web(query: str) -> str:
    """Search the web for a query."""
    print(query)
    tavily_client = TavilyClient(api_key=tavilyApiKey)
    response = tavily_client.search(query)
    print(response)
    return str(response)

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)