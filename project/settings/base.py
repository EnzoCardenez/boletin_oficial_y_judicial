import sys
import os

import environ

from django.utils.translation import gettext_lazy as _


ROOT_DIR = environ.Path(__file__) - 3
PROJECT_DIR = ROOT_DIR.path('project')
APPS_DIR = PROJECT_DIR.path('apps')

sys.path.insert(0, str(APPS_DIR))

# Load operating system environment variables and then prepare to use them
env = environ.Env()
#  patch for https://github.com/joke2k/django-environ/issues/119
env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

# PROJECT
PROJECT_NAME_HEADER = env('PROJECT_NAME_HEADER', default='Project Name')
PROJECT_NAME_TITLE = env('PROJECT_NAME_TITLE', default='Project Name')

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!!')        # noqa
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='*')       # noqa

DATABASES = {
    "default": {
        "ENGINE": os.environ.get('DB_ENGINE'),
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT'),
        }
}

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework_json_api',
    'django_filters',
    'corsheaders',
    'django_recaptcha',
    'oauth2_provider',
)

PROJECT_APPS = (
    'core',
    'administrativo',
    'organismo',
    'persona',
    'publicacion',
    'usuario',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS


MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',

)

ROOT_URLCONF = 'project.urls'

AUTH_USER_MODEL = 'usuario.Usuario'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = env.str('DJANGO_TIME_ZONE', default='America/Argentina/Catamarca')
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('es', _('Español')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = str(PROJECT_DIR.path('static'))
STATIC_URL = '/static/'

MEDIA_ROOT = str(PROJECT_DIR.path('media'))
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(PROJECT_DIR.path('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_URL = '/admin/login/'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'PAGE_SIZE': 50,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework_json_api.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'SEARCH_PARAM': 'filter[search]',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'oauth2_provider.backends.OAuth2Backend',
)


ACTIVAR_HERRAMIENTAS_DEBBUGING = env.bool('ACTIVAR_HERRAMIENTAS_DEBBUGING', default=True)

if ACTIVAR_HERRAMIENTAS_DEBBUGING:
    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions',
    )

    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

RECAPTCHA_PUBLIC_KEY = env.str(var='RECAPTCHA_PUBLIC_KEY', default="")
RECAPTCHA_PRIVATE_KEY = env.str(var='RECAPTCHA_PRIVATE_KEY', default="")
