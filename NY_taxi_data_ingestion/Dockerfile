FROM python:3.12.2-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /Data_engineering/NY_taxi_data_ingestion
ENV PATH="/Data_engineering/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY ingest_data.py .

ENTRYPOINT ["uv", "run", "python", "ingest_data.py]
