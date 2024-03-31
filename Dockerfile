FROM python:alpine
WORKDIR /app

RUN apk add --no-cache poetry tini
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install --no-root --no-dev \
    && rm -rf /root/.cache/*

COPY mmdb_whois_server mmdb_whois_server

ENTRYPOINT ["tini", "--", ".venv/bin/python", "-m", "mmdb_whois_server", "--host", "0.0.0.0"]
