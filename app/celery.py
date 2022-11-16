import os
from celery import Celery
from celery import schedules
from django.conf import settings
# from . import celeryconfig
os.environ.setdefault("DJANGO_SETTINGS_MODULE","app.settings")

app = Celery('app')
# app.config_from_object("django.conf:settings")
app.conf.enable_utc = False
app.conf.update(timezone="Africa/Cairo")
app.config_from_object(settings, namespace='CELERY')


app.autodiscover_tasks()
# app.conf.beat_schedule={ 
#     "test":{
#         "task":"Maps.tasks.test_task",
#         "schedule":schedules.crontab(hour=6,minute=4),
#         "args":(2,4)        #to pass args
#     }
    
# }
