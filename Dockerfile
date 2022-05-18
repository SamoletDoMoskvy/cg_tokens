FROM python:3.10

# Set environment varibles
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 POETRY_VIRTUALENVS_CREATE=0 SOURCE_DIR=/ WORK_DIR=/cg_backend

RUN apt-get update && apt-get upgrade -y && apt-get install -y vim nano

# Set work directory
WORKDIR app

# Upgrade pip and install poetry
RUN python -m pip install --upgrade pip && pip install poetry

# Copy poetry files
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install

# Copy project
COPY . .
