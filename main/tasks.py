# tasks.py
# Импортируем созданный нами ранее экземпляр класса celery(app)
from something.celery import app


@shared_task
def adding_task(x, y):
    return x + y
