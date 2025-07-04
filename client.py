import asyncio
import httpx
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig, RemoteMCPServer


# this will be replaced with our internal auth from internal-llm-tools
class CustomAuth(httpx.Auth):
    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request):
        request.headers["X-API-Key"] = self.token
        yield request


client = Client(
    MCPConfig(
        mcpServers={
            # "calendar_noauth": RemoteMCPServer(
            #     url="http://localhost:8000/mcp/",
            #     transport="streamable-http"
            # ),
            "calendar_auth": RemoteMCPServer(
                url="http://localhost/mcp/",
                transport="streamable-http",
                auth=CustomAuth(token="secret-key"),
            ),
        }
    )
)


async def main():
    async with client:
        tools = await client.list_tools()
        for tool in tools:
            print("=" * 40)
            print(f"Tool: {tool.name}, Description: {tool.description}")
            response = await client.call_tool(name=tool.name)
            print(f"Response from {tool.name}: {response}\n\n")


if __name__ == "__main__":
    asyncio.run(main())
