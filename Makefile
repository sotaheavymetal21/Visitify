APP_CONTAINER_NAME = app
DB_CONTAINER_NAME = mysql
RUN_APP = docker-compose exec $(APP_CONTAINER_NAME)
RUN_DJANGO = python manage.py
RUN_PYTEST = pytest

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

loaddata:
	$(RUN_DJANGO) loaddata crm.json

run:
	$(RUN_DJANGO) runserver
makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

show_urls:
	$(RUN_DJANGO) show_urls

shell:
	$(RUN_DJANGO) debugsqlshell

superuser:
	$(RUN_DJANGO) createsuperuser

test:
	$(RUN_PYTEST)

test-cov:
	$(RUN_PYTEST) --cov=application/tests/

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .

update:
	$(RUN_APP) poetry update

app:
	docker exec -it $(APP_CONTAINER_NAME) bash

db:
	docker exec -it $(DB_CONTAINER_NAME) bash