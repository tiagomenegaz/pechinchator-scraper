FROM python:3.7-alpine
MAINTAINER Leonardo Flores <contato@leonardocouy.com>

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base python-dev libffi-dev \
    py3-lxml libxslt-dev openssl-dev zlib-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

RUN apk add --no-cache libxslt openssl libstdc++

COPY . /app
