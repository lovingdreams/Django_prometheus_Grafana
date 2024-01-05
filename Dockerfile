FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN	pip install gunicorn
RUN  pip install django-prometheus

# Install Prometheus client for Python
RUN pip install prometheus_client

COPY ./my_project /app

WORKDIR /app

RUN python manage.py migrate

