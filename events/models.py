from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200)

class Event(models.Model):
    event = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_event')
    updated_on = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, name="location")
    description = models.TextField()
    participants = models.IntegerField(default=0)
