from django.db import models
from .utils import (
    TimestampModel,
)
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Notifications(TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Car(TimestampModel):
    name = models.TextField(max_length=100)
