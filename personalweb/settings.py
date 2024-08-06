from pathlib import Path, os
import sys
import dj_database_url
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTION = os.getenv("DJANGO_PRODUCTION",False)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

if PRODUCTION:  
    ALLOWED_HOSTS = ['dev.rafaelcosquiere.com']
    CSRF_TRUSTED_ORIGINS = ['https://dev.rafaelcosquiere.com']
    CSRF_COOKIE_SECURE = True

    DEBUG = False
else:
    ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.1.113']
    DEBUG = True


# Application definition

INSTALLED_APPS = [
    # django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.redirects',
    
    # own 
    'notes.apps.NotesConfig',
    'projects.apps.ProjectsConfig',
    'pages.apps.PagesConfig',

    # third party
    'easy_thumbnails',
    'filer',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
]

ROOT_URLCONF = 'personalweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'personalweb.utils.global_context.global_variables',
            ],
            'builtins': ['personalweb.utils.markdown_processor']
        },
    },
]

WSGI_APPLICATION = 'personalweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if PRODUCTION:
    # postgres configuration
    # DATABASES = {
    # "default": dj_database_url.parse(os.environ.get("DJANGO_DB_URI"))
    # }
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "database/rcdb.sqlite3",
    }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
    }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# not sure this is working as static are serve by nginx
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


SITE_ID = 1
DOMAIN = "dev.rafaelcosquiere.com"
SITE_NAME = "dev.rafaelcosquiere.com"

# SEO SETTINGS BY DEFAULT

""" 
Default valur for  <meta name="robots" content="index/noindex follow/nofollow">

if set to true, can be override by individual entries like note and pages.
if set to false, cannot be overwritten downstream

SEO_INDEX True will enable sitemaps and False disable sitemaps
"""

SEO_INDEX = True    # Default value for <meta name="robots" content="index/noindex">
SEO_FOLLOW = True   # Default value for <meta name="robots" content="follow/nofollow">


# django filer
FILER_CANONICAL_URL = 'display/'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
