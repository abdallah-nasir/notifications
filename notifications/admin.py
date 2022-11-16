from django.contrib import admin
from .models import (
    Notifications,
    Car
)
# Register your models here.

admin.site.register(Notifications)
admin.site.register(Car)
