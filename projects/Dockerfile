# Python slim base
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (psycopg2 etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Install requirements first (better layer caching)
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# Copy project
COPY . .

# Collect static at build (optional; see note below)
# You can skip this and run in a Render build command instead.
# Make sure settings.py has STATIC_ROOT set.
# RUN python manage.py collectstatic --noinput

# Expose is optional for Render, but harmless
EXPOSE 8000

# Start Gunicorn, bind to Render's $PORT
# !! Replace `myproject` with your Django project package name !!
CMD ["bash", "-lc", "gunicorn myproject.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3 --timeout 120"]
