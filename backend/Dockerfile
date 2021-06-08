FROM python:3.8-alpine

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

COPY scripts/start.sh /

COPY . /code/