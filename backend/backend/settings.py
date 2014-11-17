"""
Django settings for backend project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.dirname(__file__)

CONFIG_FILE = os.path.join(BASE_DIR, 'config/local.env')

config_vars = open(CONFIG_FILE).readlines()
for l in config_vars:
    s = l.split('=')
    os.environ[s[0].strip()] = s[1].strip()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY').strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'custom_user.EmailUser'

# Application definition

INTERNAL_APPS = (
)

EXTERNAL_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'custom_user',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',  
)

INSTALLED_APPS = INTERNAL_APPS + EXTERNAL_APPS

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer', # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser', # Any other parsers
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # optional
    ),
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'localhost:4200',
)


ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': os.environ.get('BACKEND_DB_NAME', 'backend_db'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.environ.get('POSTGRES_DB_USER', 'MDee'),
        'PASSWORD': os.environ.get('POSTGRES_DB_PASS', ''),
        'HOST': 'localhost',
        'PORT': '5432',
        }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
