FROM python:3.8.2-slim

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
