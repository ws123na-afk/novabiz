import os
import dj_database_url

# Render provides this at runtime — set it in the dashboard
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")

DEBUG = os.environ.get("DEBUG", "0") == "1"

# Render service hostname will be something like: myservice.onrender.com
ALLOWED_HOSTS = ["localhost", "127.0.0.1"] + os.environ.get("ALLOWED_HOSTS", "").split(",")

# Database (Render sets DATABASE_URL). Add sslrequire for Postgres.
DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# WhiteNoise (serve static in Docker)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... the rest
]

# Better static performance
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
