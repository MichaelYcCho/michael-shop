from .base import *


# Docker Secrets 파일을 읽어서 env로 활용
def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

DJANGO_KAKAO_ID = read_secret('DJANGO_KAKAO_ID')

ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'michael_shop',
        "USER": 'michael',
        "PASSWORD": read_secret('POSTGRES_PASSWORD'),
        "HOST": '158.247.224.15',
        "PORT": 5432,
    }
}
