env:
	pipenv shell

renv:
	python3 -m venv venv

install:
	pipenv install

rinstall:
	source venv/bin/activate && pip install -r requirements.txt

run:
	python3 manage.py runserver

dev:
	python3 manage.py runserver 0.0.0.0:8000

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

check:
	python3 manage.py check

user:
	python3 manage.py createsuperuser

test:
	python3 manage.py test

behave:
	tests/integration