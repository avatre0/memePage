# syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py ./
COPY templates/ ./templates/

ENTRYPOINT ["gunicorn", "-b :5000", "main:create_app()"]