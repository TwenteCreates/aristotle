migrate:
	python3 manage.py makemigrations --no-input
	python3 manage.py migrate --no-input

build:
	docker build -t mauritso/aristotle-api .

push: build
	docker push mauritso/aristotle-api

deploy: push
	ssh aristotle-api ./deploy.sh

dev:
	HOST=127.0.0.1 DEBUG=True python3 manage.py runserver
