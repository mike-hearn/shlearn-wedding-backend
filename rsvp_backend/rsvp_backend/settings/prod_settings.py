import os

from .base_settings import *

DEBUG = True

ALLOWED_HOSTS = ['shleyandhearn.mikehearn.com', 'shleyandhearn.com',
                 'www.shleyandhearn.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432'
    }
}
