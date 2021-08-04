# Local devs


## Prepare Python env (first time)

$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt

## Required configs with a local Postgresql server

Prepare a `.env` file:

export DB_NAME=covary
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_HOST=localhost
export DB_PORT=5432
export DJANGO_ALLOWED_HOSTS=*
export DEBUG=1

## Launch dev env 

$ source ./venv/bin/activate

First time:

$ ./manage.py collectstatic --noinput
$ ./manage migrate
$ ./manage.py createsuperuser

Each time:
$ ./manage runserver


Open http://localhost:8000/admin/

## Create and run local container for test with local db

$ docker build . -t gfoo/covary-backend
# for debug add -e DEBUG=1
$ docker run --net=host -e DB_HOST=127.0.0.1 -e DB_PORT=5432 -e DB_NAME=postgres -e DB_USER=postgres -e DB_PASSWORD=postgres -e DJANGO_ALLOWED_HOSTS=* -it gfoo/covary-backend

