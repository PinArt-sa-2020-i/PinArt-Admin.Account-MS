FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

COPY docker-entrypoint.sh /usr/bin/

RUN chmod +x /usr/bin/docker-entrypoint.sh

# Server

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
