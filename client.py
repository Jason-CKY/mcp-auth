import asyncio
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig, RemoteMCPServer
from fastmcp.client.auth import BearerAuth


# Load api key from token.txt
with open("token.secret", "r") as f:
    api_key = f.read().strip()

client = Client(
    MCPConfig(
        mcpServers={
            "calendar": RemoteMCPServer(
                url="http://localhost:8000/mcp",
                transport="streamable-http"
            ),
            "authenticated calendar": RemoteMCPServer(
                url="http://localhost:8001/mcp",
                transport="streamable-http",
                auth=BearerAuth(api_key),
            ),
        }
    )
)

async def main():
    async with client:
        print(await client.list_tools())

if __name__ == "__main__":
    asyncio.run(main())