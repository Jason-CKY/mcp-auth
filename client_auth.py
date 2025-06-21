import asyncio
import os
from fastmcp import Client
from fastmcp.client.auth import BearerAuth
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")

async def main():
    async with Client(
        "http://localhost:8001/mcp", 
        auth=BearerAuth(token=api_key),
    ) as client:
        print(client.transport)
        print(await client.list_tools())
    
if __name__ == "__main__":
    asyncio.run(main())