FROM python:3.9


ENV PYTHONUNBUFFERED 1

RUN mkdir /drf

WORKDIR /drf

ADD . /drf/

RUN pip install -r requirements.txt