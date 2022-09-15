from celery import Celery
import resize
app = Celery('celery_worker', broker ='pyamqp://guest@localhost//')


@app.task
def task1(image_pass):
    resize.resizer(image_pass)
    return True