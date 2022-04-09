from celery.utils.log import get_task_logger
from time import sleep

from asyncjob.celery import app

logger = get_task_logger(__name__)


@app.task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    print('*' * 100)
    print('>> Oops!')
    print('.' * 100)
    return ('first_task_done')


# normal function call in python
my_first_task(1)
# add task to the celery with function call
my_first_task.delay(9)
