from pathlib import Path

from .env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent

# Production
PRODUCTION = env("PRODUCTION", default=False, cast=bool)

THEME_PARTY_APPS = [
    'rest_framework',
    'debug_toolbar',
    'corsheaders',
    'djmoney',
]

APPS = [
    'distributor',
    'product',
    'users',
    'transaction',
]

THEME = [
    'jazzmin'
]

INSTALLED_APPS = [
    *THEME,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THEME_PARTY_APPS,
    *APPS
]
# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True


USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.joinpath("static")

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 13,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny"
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

from .cors import *

if not PRODUCTION:
    from .local import *
else:
    from .prod import *

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

from .jazzmin import JAZZMIN_SETTINGS
