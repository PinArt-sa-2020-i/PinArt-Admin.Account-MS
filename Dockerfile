FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV SRC = /code

RUN mkdir $SRC

WORKDIR $SRC

ADD requirements.txt $SRC/

RUN pip install -r requirements.txt

ADD . $SRC/
