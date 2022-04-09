from celery.utils.log import get_task_logger
from time import sleep

logger = get_task_logger(__name__)


@task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return ('first_task_done')


# normal function call in python
my_first_task()
# add task to the celery with function call
my_first_task.delay()
