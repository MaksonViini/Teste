# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app
ENV FLASK_APP main.py

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .  
# Copia tudo que temos para o diretório raiz /app

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]