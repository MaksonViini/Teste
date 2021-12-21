FROM python:3.9-slim

COPY . /Books
COPY . /requirements.txt 

WORKDIR /Books

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]