FROM python:3.13.3

# Directory
ARG ROOT_DIR="/nlp100-python"
WORKDIR ${ROOT_DIR}

# Poetry
ENV POETRY_VERSION=2.1.3
ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

# Dependencies
ADD pyproject.toml ${ROOT_DIR}/pyproject.toml
ADD poetry.lock ${ROOT_DIR}/poetry.lock
RUN poetry install --no-root

# Source
ADD . ${ROOT_DIR}
