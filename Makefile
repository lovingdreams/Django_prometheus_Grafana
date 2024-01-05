SHELL := /bin/bash

.PHONY: env-setup run-local pre-push

env-setup:
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt;

migrations: env-setup
	source venv/bin/activate; \
	python manage.py makemigrations; \
    python manage.py migrate; \


run-local: env-setup
	source venv/bin/activate; \
	python manage.py makemigrations; \
    python manage.py migrate; \
    python manage.py runserver;
