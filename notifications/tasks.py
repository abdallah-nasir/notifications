from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notifications
import json
from celery import Celery, states
from celery.exceptions import Ignore
import asyncio
from datetime import datetime as dt


@shared_task
def broadcast_notification(**kwargs): 
    # try:
    notification_id = int(kwargs.get("id"))
    notification = Notifications.objects.get(id=notification_id)
    channel = get_channel_layer()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    async_func = channel.group_send(
        "notification_abdallah",
    {
        "type": "send_notification",
        "message": notification.title,
    }
    )
    loop.run_until_complete(async_func)
    return "Done"

    # except Exception:
    #     # self.update_state(
    #     #     state='FAILURE',
    #     #     meta={
    #     #         "exe":"Not Found",
    #     #     }
           
    #     # )
    #     raise Ignore()  
