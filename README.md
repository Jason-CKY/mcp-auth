# MCP Auth Example

This project demonstrates how to run a FastMCP server with Bearer authentication. It includes both authenticated and unauthenticated endpoints, as well as example clients and key/token generation scripts.

## Features

- **FastMCP server** with and without authentication
- **Bearer token authentication** using RSA key pairs
- **Example Python clients** for both endpoints
- **Key and token generation utility**

## Project Structure

```sh
.
├── client.py              # Example client for both endpoints
├── client_auth.py         # Client for authenticated endpoint
├── server.py              # Unauthenticated MCP server (port 8000)
├── server_auth.py         # Authenticated MCP server (port 8001)
├── generate_keys.py       # Script to generate RSA keys and a test token
├── token.secret           # Generated Bearer token (ignored in .gitignore)
├── public_key.pem         # Generated public key for server auth
├── Dockerfile             # Dockerfile for MCP server
├── nginx.conf             # Nginx config for Bearer auth
├── docker-compose.yml     # Docker Compose setup
├── pyproject.toml         # Python project config
└── README.md              # This file
```

## Quick Start

### 1. Generate Keys and Token

Run the following to generate an RSA key pair and a test Bearer token:

```sh
uv run generate_keys.py
```

This creates `public_key.pem` and `token.secret`.

### 2. Build and Start Services

```sh
uv run server.py
uv run server_auth.py
```

- MCP server (unauthenticated): <http://localhost:8001/mcp/>
- MCP server (authenticated, via Nginx): <http://localhost/mcp/>

### 3. Test the Clients

#### Unauthenticated

```sh
uv run client.py
```

#### Authenticated

```sh
uv run client_auth.py
```

Or use the `client.py` to test both endpoints (see code for details).

## How It Works

- **server.py**: Runs a FastMCP server on port 8000 (no auth).
- **server_auth.py**: Runs a FastMCP server on port 8001 with Bearer authentication using the public key.
- **client.py / client_auth.py**: Example clients that use the Bearer token from `token.secret`.

## Customization

- To use your own keys or tokens, modify and rerun `generate_keys.py`.

## Requirements

- Uv
- [fastmcp](https://pypi.org/project/fastmcp/)

## License

MIT
