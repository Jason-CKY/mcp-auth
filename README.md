# MCP Auth Example

This project demonstrates a FastMCP server with both authenticated and unauthenticated endpoints. Bearer token authentication is enforced at the Nginx proxy layer. Envoy acts as a reverse proxy, forwarding requests to the MCP server and integrating with Open Policy Agent (OPA) for fine-grained authorization decisions. The repository includes example clients and a Docker setup for running all components together.

## Features

- FastMCP server with and without authentication
- Example Python clients for both endpoints
- Docker Compose setup with Nginx, Envoy, and OPA integration

## Project Structure

```sh
.
├── Dockerfile              # Dockerfile for MCP server
├── README.md
├── client.py               # Example client for both endpoints
├── docker-compose.yml      # Docker Compose setup (Nginx, Envoy, OPA, MCP)
├── proxy
│   ├── envoy               # Envoy config
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── envoy.yaml
│   ├── nginx.conf          # Nginx config for Bearer auth
│   └── policy.rego         # OPA policy for Envoy
├── pyproject.toml          # Python project config
├── server.py               # Unauthenticated MCP server (port 8000)
└── uv.lock
```

## Quick Start

### 1. Install Dependencies

Install Python dependencies (requires uv):

```sh
uv sync
```

### 2. Build and Start Services

Build and start all services using Docker Compose:

```sh
docker compose up --build -d
```

- MCP server (unauthenticated): <http://localhost:8000/mcp/>
- MCP server (authenticated, via Nginx): <http://localhost/mcp/>

### 3. Test the Clients

#### Unauthenticated

```sh
uv run client.py
```

#### Authenticated

Edit `client.py` to use the authenticated endpoint and provide a valid token.

## How It Works

- `server.py`: Runs a FastMCP server on port 8000 (no auth).
- `client.py`: Example client for both endpoints, supports custom authentication.
- `proxy/`: Contains Nginx and Envoy configs for authentication and policy enforcement.

## Requirements

- [fastmcp](https://pypi.org/project/fastmcp/)
- Docker & Docker Compose
- [uv](https://github.com/astral-sh/uv) (for Python dependency management)
