"""
Django settings for scipertise_demo project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import logging

#db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES[‘default’].update(db_from_env)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMINS = (('Leigh', 'leigh.christopher2@gmail.com'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

#API_KEY ='46235562'

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

#DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'cryptic-dawn-32564.herokuapp.com']

#DATABASES = { 'default': dj_database_url.config() }

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'pages',
    'users',
    'search',
    'taggit',
    'booking',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'widget_tweaks',
    'sendgrid',
 
  
 
   
  
]

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
#        'URL': 'http://127.0.0.1:9200/',
#        'INDEX_NAME': 'haystack',
#    },
#}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
BOOTSTRAP4 = {
    'include_jquery': True,
}

SITE_ID = 1

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = 'scipertise_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'scipertise_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL'
    )
}
#
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}



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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = "/media/"
#MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

TAGGIT_CASE_INSENSITIVE = True

#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'EMAIL_HOST_USER'
#EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'founders@scipertise.com'
#
#SENDGRID_API_KEY='SENDGRID_API_KEY'
#SENDGRID_PASSWORD='SENDGRID_PASSWORD'
#SENDGRID_USERNAME='SENDGRID_USERNAME'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_PORT = 587

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'formatters': {
#        'verbose': {
#            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
#        },
#    },
#    'handlers': {
#        # Send all messages to console
#        'console': {
#            'level': 'DEBUG',
#            'class': 'logging.StreamHandler',
#        },
#
#        # Warning messages are sent to admin emails
#        'mail_admins': {
#            'level': 'WARNING',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler',
#        },
#        # critical errors are logged to sentry
#        'sentry': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'raven.contrib.django.handlers.SentryHandler',
#        },
#    },
#    'loggers': {
#        # This is the "catch all" logger
#        '': {
#            'handlers': ['console', 'syslog', 'mail_admins', 'sentry'],
#            'level': 'DEBUG',
#            'propagate': False,
#        },
#    }
#}

# Activate Django-Heroku.
django_heroku.settings(locals())





