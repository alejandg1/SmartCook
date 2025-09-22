import mimetypes
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)pts(%0!ibqd^-h5m6+d*-53bdixr)izrf28i20+0+to3+0o=e'

DEBUG = True
mimetypes.add_type("text/css", ".css", True)

ALLOWED_HOSTS = ['*']

ALLOWED_ORIGINS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000',
                        'https://smartcook.up.railway.app',
                        'http://172.0.0.1:8000'
                        ]

INSTALLED_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smartcook',
    'security',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'application.wsgi.application'


DATABASES = {
    'default': {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ.get("DATABASE_NAME", "smartcook_db"),
    "USER": os.environ.get("DATABASE_USER", "smartcook_user"),
    "PASSWORD": os.environ.get("DATABASE_PASSWORD", "smartcook_pass"),
    "HOST": os.environ.get("DATABASE_HOST", "db"),
    "PORT": os.environ.get("DATABASE_PORT", "5432")
    }
}


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


LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap5'


AUTH_USER_MODEL = "security.User"
LOGIN_URL = 'security:login'
LOGIN_REDIRECT_URL = 'security:profile'
LOGOUT_REDIRECT_URL = 'smartcook:index'
SINGIN_REDIRECT_URL = 'smartcook:index'
SINGIN_URL = 'security:singin'
