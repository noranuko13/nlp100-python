FROM python:3.14.3

# Directory
ARG ROOT_DIR="/nlp100-python"
WORKDIR ${ROOT_DIR}

# uv
ENV UV_PROJECT_ENVIRONMENT=/usr/local
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Dependencies
COPY pyproject.toml uv.lock ${ROOT_DIR}/
RUN uv sync --frozen --no-install-project
