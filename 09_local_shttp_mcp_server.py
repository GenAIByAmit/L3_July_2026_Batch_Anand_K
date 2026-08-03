from fastmcp import FastMCP

mcp_server = FastMCP("Local MCP shttp server")

@mcp_server.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp_server.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp_server.run(transport="http", port=8000) #default protocol is shttp
