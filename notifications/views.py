from django.shortcuts import render
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from channels.layers import get_channel_layer
from .models import (
    Notifications,
)
# Create your views here.


def main(request):
    template = "main.html"
    notifications = Notifications.objects.select_related("user").filter(status=False)
    context = {
        "room_name": "abdallah",
        "notifications": notifications,
    }
    return render(request, template, context)


def test(request):
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        "notification_abdallah",
    {
        "type": "send_notification",
        "message": "Congratulation",
    }
    )
    return HttpResponse("Done")