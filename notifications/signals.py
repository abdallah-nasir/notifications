from .models import Notifications, Car
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import MINUTES, PeriodicTask, CrontabSchedule, PeriodicTasks
import json
from .tasks import broadcast_notification

@receiver(post_save, sender=Car)
def notification_handler(sender, instance, created, **kwargs):
    # # call group_send function directly to send notificatoions or you can create a dynamic task in celery beat
    notification = Notifications.objects.create(user_id=1, title="car created")
    data = json.dumps({"id": notification.id})

    if created:
        # for schedule task of notification
        broadcast_notification.delay(**{"id": notification.id})
        # schedule, created = CrontabSchedule.objects.get_or_create(hour = instance.created_at.hour + 2, minute = instance.created_at.minute + 1, day_of_month = instance.created_at.day, month_of_year = instance.created_at.month)
        # task = PeriodicTask.objects.create(crontab=schedule, name=f"broadcast-notification-{instance.id}", task="notifications.tasks.broadcast_notification", kwargs=data)
    else:
        broadcast_notification.delay(**{"id": notification.id})
