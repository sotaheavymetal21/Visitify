RUN_DJANGO = python manage.py
RUN_PYTEST = pytest


run:
	$(RUN_DJANGO) runserver
makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

showmigrations:
	$(RUN_DJANGO) showmigrations

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
