# Python environment management
env:
	pipenv shell

renv:
	python3 -m venv venv

install:
	pipenv install

rinstall:
	source venv/bin/activate && pip install -r requirements.txt

# Run the development server
run:
	python3 manage.py runserver

dev:
	python3 manage.py runserver 0.0.0.0:8000

# Database migrations
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

# Project checks
check:
	python3 manage.py check

# Create superuser
user:
	python3 manage.py createsuperuser

# Run tests
test:
	python3 manage.py test

# Run integration tests
integration:
	cd tests/integration && behave

# Display help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  env          Activate pipenv shell"
	@echo "  renv         Create virtual environment using venv"
	@echo "  install      Install dependencies using pipenv"
	@echo "  rinstall     Install dependencies from requirements.txt"
	@echo "  run          Run the Django development server"
	@echo "  dev          Run the Django dev server on 0.0.0.0:8000"
	@echo "  migrate      Run makemigrations and migrate"
	@echo "  check        Run Django system checks"
	@echo "  user         Create a Django superuser"
	@echo "  test         Run Django tests"
	@echo "  integration  Run integration tests using behave"
