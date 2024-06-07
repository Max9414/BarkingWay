from django.urls import path
from .views import *

urlpatterns = [
    path('', EventList.as_view(), name='event_list'),
    path('create-event', event_form_view, name='create_event'),
    path('event-detail/<int:event_id>', event_detail, name='event_detail'),
    path('create-location', create_location, name='create_location'),
    path('event-detail/<int:event_id>/edit', event_form_view, name='modify_event'),
]