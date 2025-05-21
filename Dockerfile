FROM python:3.13.3

# Directory
ARG ROOT_DIR="/nlp100-python"
WORKDIR ${ROOT_DIR}

# Poetry
ENV POETRY_VERSION=2.1.3
ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

# Dependencies
COPY pyproject.toml poetry.lock ${ROOT_DIR}/
RUN poetry install --no-root
