from celery import shared_task
from .views import ClearTask
from .models import Task
@shared_task
def ClearTask():
    Task.objects.filter(done=True).delete()
    print('tasks deleted')