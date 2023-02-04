from celery import Celery

app = Celery(
    broker="pyamqp://guest@localhost//"
)

@app.task
def hello_world():
    return "Ola mundo"

