from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Model to manage location (cities)
class Location(models.Model):
    location = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["location"]

    def __str__(self):
        return self.location


class EventQuerySet(models.QuerySet):
    def upcoming_events(self):
        today = timezone.now().date()
        return self.filter(event_date__gte=today) #checks if event_date is
        # gte (Greater Than or Equal to) today

# Model to manage events, connected to both Location and User db
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

    objects = EventQuerySet.as_manager() #defines custom querysets with asmanager

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.event

    # both used to add or remove participants from the event.
    def add_participants(self):
        self.participants +=1
        self.save()

    def remove_participants(self):
        self.participants -=1
        self.save()


