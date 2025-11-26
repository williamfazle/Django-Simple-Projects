# myblog/settings.py
"""
Django settings for myblog project.
Copy this whole file over your existing settings.py (replace).
Designed for local development (DEBUG=True). Before production:
 - set DEBUG=False
 - provide a secure DJANGO_SECRET_KEY in environment
 - set ALLOWED_HOSTS appropriately
"""

from pathlib import Path
import os

# ---------------------------
# Basic paths & secrets
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Get secret from env if set, otherwise use a dev fallback (DO NOT use dev fallback in production)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-this')

# Turn this False when deploying for real
DEBUG = True

# Keep this for local dev; change when deploying to PythonAnywhere / other host
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ---------------------------
# Installed apps
# ---------------------------
INSTALLED_APPS = [
    # Django contrib apps (required for admin/auth to work)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your app
    'posts.apps.PostsConfig',

    # Your apps:
    # 'posts.apps.PostsConfig',
]

# ---------------------------
# Middleware (order matters)
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',        # must be before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',     # requires sessions
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------
# URL conf & WSGI
# ---------------------------
ROOT_URLCONF = 'myblog.urls'
WSGI_APPLICATION = 'myblog.wsgi.application'

# ---------------------------
# Templates (admin needs DjangoTemplates backend)
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # global templates dir (optional) + app templates via APP_DIRS=True
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',   # required by admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------------------
# Database (simple, zero-config SQLite for dev)
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------------
# Password validation (default)
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ---------------------------
# Internationalization
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------
# Static / media
# ---------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')   # used by collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------------------
# Default primary key field type
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
