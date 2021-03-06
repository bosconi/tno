# -*- coding: utf-8 -*-
"""
Django settings for tno project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import print_function, unicode_literals
import os

from core.utils import abspath

from .conf.pipeline import *  # noqa


# where manage.py is located
PROJECT_PATH = abspath(__file__, '..', '..', '..')
# project name - name of PROJECT_PATH inside PROJECT_ROOT
PROJECT_NAME = os.path.basename(abspath(__file__, '..', '..'))

INSTALLED_APPS = [
    'core',
    'onetime',

    'braces',
    'crispy_forms',
    'django_auxilium',
    'djangosecure',
    'pipeline',
    'rest_framework',
    'vanilla',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auxilium.middleware.html.MinifyHTMLMiddleware',
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media files
MEDIA_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, 'media')
MEDIA_URL = '/media/'

# Static files
STATIC_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, 'all_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, PROJECT_NAME, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_LESS_ARGUMENTS = '--include-path="{}"'.format(
    ':'.join(STATICFILES_DIRS)
)

# Templates
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(PROJECT_PATH, PROJECT_NAME, 'templates'),
    ],
    # 'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
        'allowed_include_roots': STATICFILES_DIRS,
    },
}]

# URLs
ROOT_URLCONF = 'tno.urls'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
WSGI_APPLICATION = 'tno.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s '
                      '%(levelname)s '
                      '%(name)s '
                      '%(message)s'
        },
        'simple': {
            'format': '%(levelname)s '
                      '%(name)s '
                      '%(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'INFO',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'onetime': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    }
}
