from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server import FastMCP

with open("public_key.pem", "r") as f:
    public_key_pem = f.read()

auth = BearerAuthProvider(public_key=public_key_pem)


mcp = FastMCP(name="My Authenticated MCP Server", auth=auth)


@mcp.tool
def greet_with_auth(name: str) -> str:
    return f"Authenticated Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8001)
