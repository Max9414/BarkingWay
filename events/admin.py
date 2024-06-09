from django.contrib import admin
from .models import Event, Location, EventParticipant

# Register your models here.

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(EventParticipant)