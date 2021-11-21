from .base import *
from decouple import config


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = config('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'michael_shop',
        "USER": 'michael',
        "PASSWORD":  config('DB_PASSWORD'),
        "HOST": '158.247.224.15',
        "PORT": 5432,
    }
}
