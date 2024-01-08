FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update \
   && apt-get install -y libpq-dev \
   && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2
RUN pip install psycopg2-binary

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN     pip install gunicorn
RUN  pip install django-prometheus

RUN pip install prometheus_client

COPY ./my_project /app

WORKDIR /app

RUN python manage.py migrate