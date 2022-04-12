from celery import shared_task


@shared_task
def adding_task(time):
    return f'Message from {time}'
