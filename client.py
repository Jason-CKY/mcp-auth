import asyncio
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig, RemoteMCPServer

"""
"""

client = Client(
    MCPConfig(
        mcpServers={
            "calendar": RemoteMCPServer(
                url="http://localhost:8000/mcp/",
                transport="streamable-http"
            ),
            "authenticated calendar": RemoteMCPServer(
                url="http://localhost/mcp/",
                transport="streamable-http",
            ),
        }
    )
)

async def main():
    async with client:
        print(await client.list_tools())

if __name__ == "__main__":
    asyncio.run(main())