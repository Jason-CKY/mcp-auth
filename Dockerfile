FROM python:3.12-slim AS base

FROM base AS builder
COPY --from=ghcr.io/astral-sh/uv:0.7.12 /uv /bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /code
COPY uv.lock pyproject.toml /code/
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked --no-install-project --no-dev
COPY . /code
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked --no-dev

FROM base AS production
WORKDIR /code

# Create a non-root user and group
RUN groupadd -g 2000 appgroup \
    && useradd -u 1000 -g 2000 -m appuser
    
COPY --from=builder /code /code
ENV PATH="/code/.venv/bin:$PATH"

# Set file permissions for non-root user
RUN chown -R 1000:2000 /code

# Switch to non-root user
USER 1000:2000

EXPOSE 8080

CMD ["python", "server.py"]
