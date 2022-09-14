from celery import Celery

app = Celery('celery_worker', broker ='pyamqp://guest@localhost//')


@app.task
def task1():
    return "ok!"