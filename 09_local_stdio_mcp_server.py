from fastmcp import FastMCP

mcp_server = FastMCP("Local MCP stdio server")

@mcp_server.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp_server.run() #default protocol is stdio
