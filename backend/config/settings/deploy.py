from .base import *
from decouple import config


# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = config('DJANGO_SECRET_KEY')

DJANGO_KAKAO_ID = config('DJANGO_KAKAO_ID')

ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'michael_shop',
        "USER": 'michael',
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": '158.247.224.15',
        "PORT": 5432,
    }
}
