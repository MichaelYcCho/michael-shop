FROM python:3.10.0-buster

WORKDIR /home/

RUN echo "1.0.4"

RUN git clone https://github.com/michael-cho77/michael-shop.git

WORKDIR /home/michael-shop/

RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["bash", "-c", "python manage.py collectstatic --clear --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000"]

#CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "0.0.0:8000"]