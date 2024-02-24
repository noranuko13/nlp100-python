FROM python:3.12.2

# Poetry
ENV POETRY_VERSION=1.7.1
ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python -

# Source
ADD . /nlp100-python
WORKDIR /nlp100-python
