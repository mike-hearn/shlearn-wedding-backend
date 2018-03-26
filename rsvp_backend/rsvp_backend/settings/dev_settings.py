import os

from .base_settings import *

ALLOWED_HOSTS = ['shleyandhearn.mikehearn.com', 'shleyandhearn.com',
                 'www.shleyandhearn.com', 'localhost', 'desktop.mikehearn.com']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '5432'
    }
}

DEBUG = True
