FROM python:3.8.3-alpine
WORKDIR /usr/src/app
# no .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY ./entrypoint.sh .
# copy project
COPY . .
# entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# launch django through wsgi
CMD ["sh","-c","gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]
