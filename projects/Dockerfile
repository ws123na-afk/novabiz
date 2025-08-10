FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# ...
COPY requirements.txt .

# make pip more reliable on slow networks
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip config set global.timeout 180 && \
    pip config set global.retries 10

# install deps with longer timeout & retries
RUN PIP_DEFAULT_TIMEOUT=180 pip install --no-cache-dir --default-timeout=180 -r requirements.txt
# ...

