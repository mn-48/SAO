
docker exec -it web python manage.py makemigrations

docker exec -it web python manage.py migrate

docker exec -it web python manage.py createsuperuser