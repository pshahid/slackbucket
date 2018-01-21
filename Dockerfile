FROM python:3.6

ARG commit
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT ['docker-entrypoint.sh']

