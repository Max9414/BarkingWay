from django.urls import path
from .views import EventList, event_detail, create_event, create_location

urlpatterns = [
    path('', EventList.as_view(), name='event_list'),
    path('create-event', create_event, name='create_event'),
    path('event-detail', event_detail, name='event_detail'),
    path('create-location', create_location, name='create_location')
]