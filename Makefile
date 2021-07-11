build:
	docker-compose -p servicearea up -d --build --remove-orphans

container:
	docker exec -it servicearea bash

test:
	DJANGO_SETTINGS_MODULE=settings.test_settings pytest -v service_area/tests

shell:
	./manage.py shell_plus

run:
	./manage.py runserver 0:8000

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

createsuperuser:
	./manage.py createsuperuser