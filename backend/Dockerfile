FROM python:3.10.0-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /home/michael-shop/backend/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["bash", "-c", "python manage.py collectstatic --clear --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000"]

#CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "0.0.0:8000"]