#!/bin/sh

echo "Backend: waiting for postgres host=$DB_HOST port=$DB_PORT ..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 1
done
echo "Backend: PostgreSQL started"

# deploy static files
python manage.py collectstatic --noinput
# always apply migration
python manage.py migrate
# then laucnh command
exec "$@"
