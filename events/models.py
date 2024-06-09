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
    #added a db to track who joins and leaves
    def add_participants(self, user):
        self.participants +=1
        self.save()
        EventParticipant.objects.create(event=self, user=user)

    def remove_participants(self, user):
        self.participants -=1
        self.save()
        EventParticipant.objects.filter(event=self, user=user).delete()


#As I haven't included this in the original db, I thought of a way
#to overcome this problem and link this db to the previous one
#this way, i'm able to track who participated and act accordingly
class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_attending')

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return f'{self.event} - {self.user}'

    @classmethod
    def is_attending(cls, event, user):
        return cls.objects.filter(event=event, user=user).exists()
