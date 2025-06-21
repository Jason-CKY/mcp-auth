import httpx
import asyncio
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig, RemoteMCPServer, infer_transport_type_from_url
from fastmcp.client.auth import BearerAuth
import os
from dotenv import load_dotenv
from fastmcp.client.transports import (
    SSETransport,
    StreamableHttpTransport,
)


load_dotenv()
api_key = os.getenv("API_KEY")


class RemoteMCPServerWithCustomAuth(RemoteMCPServer):
    auth: httpx.Auth

    model_config={
        "arbitrary_types_allowed": True,
    }

    def to_transport(self) -> StreamableHttpTransport | SSETransport:
        if self.transport is None:
            transport = infer_transport_type_from_url(self.url)
        else:
            transport = self.transport

        if transport == "sse":
            return SSETransport(self.url, headers=self.headers, auth=self.auth)
        else:
            return StreamableHttpTransport(
                self.url, headers=self.headers, auth=self.auth
            )


client = Client(
    MCPConfig(
        mcpServers={
            "calendar": RemoteMCPServer(
                url="http://localhost:8000/mcp",
                transport="streamable-http"
            ),
            "authenticated calendar": RemoteMCPServerWithCustomAuth(
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