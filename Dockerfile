FROM python:3.7-alpine3.8
WORKDIR /app
COPY autoFill.py /app/
RUN apk update
RUN apk add chromium chromium-chromedriver
RUN pip install --upgrade pip
RUN pip install selenium