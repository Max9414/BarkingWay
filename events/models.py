from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

class Event(models.Model):
    event = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_event')
    updated_on = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="events", null=False, blank=False)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True)
    participants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.event
