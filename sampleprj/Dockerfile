FROM python:latest

# Initialize
RUN mkdir -p /data/crudbuilder_example
WORKDIR /data/crudbuilder_example
COPY requirements.txt /data/crudbuilder_example

# Setup
RUN apt-get update
RUN apt-get install python3 python3-dev postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

# Prepare
COPY . /data/django-quickstart/
