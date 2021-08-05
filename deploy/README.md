# Stack deploy

## Required configs

Prepare a `.env` file:

```
#DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
POSTGRES_PASSWORD=postgres
BACKEND_VERSION=v1.0
DJANGO_SUPERUSER_PASSWORD=admin
```
## Launch stack

```
docker-compose up -d
docker-compose exec backend python manage.py collectstatic --no-input --clear
docker-compose exec backend python manage.py migrate --noinput
docker-compose exec backend python manage.py createsuperuser --noinput --username admin --email admin@covary.org
```


Open http://localhost:8000/admin/


