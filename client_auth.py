import asyncio
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

# Load api key from token.txt
with open("token.secret", "r") as f:
    api_key = f.read().strip()


async def main():
    async with Client(
        "http://localhost:8001/mcp", 
        auth=BearerAuth(token=api_key),
    ) as client:
        print(client.transport)
        print(await client.list_tools())
    
if __name__ == "__main__":
    asyncio.run(main())