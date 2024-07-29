docker-compose up

docker-compose down

docker-compose build

docker-compose up -d


docker exec -it web python manage.py makemigrations

docker exec -it web python manage.py migrate

docker exec -it web python manage.py createsuperuser


localhost:8000