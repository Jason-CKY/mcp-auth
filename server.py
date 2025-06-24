from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers
from loguru import logger

mcp = FastMCP("My MCP Server")


@mcp.tool
def greet() -> str:
    headers = get_http_headers()
    logger.info(f"Received headers: {headers}")
    name = headers.get("x-given-name", "unknown")
    return f"Hello, {name}!"


@mcp.tool
async def safe_header_info() -> dict:
    """Safely get header information without raising errors."""
    # Get headers (returns empty dict if no request context)
    headers = get_http_headers()

    # Get authorization header
    auth_header = headers.get("authorization", "")
    is_bearer = auth_header.startswith("Bearer ")

    return {
        "user_agent": headers.get("user-agent", "Unknown"),
        "content_type": headers.get("content-type", "Unknown"),
        "has_auth": bool(auth_header),
        "auth_type": "Bearer" if is_bearer else "Other" if auth_header else "None",
        "headers_count": len(headers),
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000, host="0.0.0.0")
