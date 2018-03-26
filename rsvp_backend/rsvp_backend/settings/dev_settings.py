import os

from .base_settings import *

ALLOWED_HOSTS = [
    'localhost',
    'desktop.mikehearn.com',
]

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
