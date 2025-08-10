import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'home','accounts','store','booking','crm','dashboard','marketplace','payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[BASE_DIR/'templates'],
    'APP_DIRS':True,
    'OPTIONS':{'context_processors':[
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'home.context_processors.brand',
    ]},
}]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}

LANGUAGE_CODE='en'
LANGUAGES=[('en','English'),('ar','Arabic')]
LOCALE_PATHS=[BASE_DIR/'locale']
TIME_ZONE='Asia/Dubai'
USE_I18N=True
USE_TZ=True

STATIC_URL='/static/'
STATIC_ROOT=BASE_DIR/'staticfiles'
STATICFILES_DIRS=[BASE_DIR/'static']

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

STORAGES={"staticfiles":{"BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"}}

# Custom
NOVABIZ_WHATSAPP=os.environ.get("NOVABIZ_WHATSAPP","056-0000000")
NOVABIZ_BRAND=os.environ.get("NOVABIZ_BRAND","NovaBiz")
NOVABIZ_MARKETPLACE_ENABLED=True

# Payments (read by payments app)
STRIPE_PUBLIC_KEY=os.environ.get("STRIPE_PUBLIC_KEY","")
STRIPE_SECRET_KEY=os.environ.get("STRIPE_SECRET_KEY","")
PAYPAL_CLIENT_ID=os.environ.get("PAYPAL_CLIENT_ID","")
PAYPAL_SECRET=os.environ.get("PAYPAL_SECRET","")
