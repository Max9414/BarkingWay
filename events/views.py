from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import Event, EventParticipant
from .forms import EventForm, LocationForm

# Create your views here.

class EventList(generic.ListView):
    """
    Display all the events from today on.
    Allows research for location and event
    date.
    """
    model = Event
    template_name = "events/event_list.html"
    context_object_name = 'events'
    paginate_by = 6


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        location_filter = self.request.GET.get('location')
        event_date_filter = self.request.GET.get('event_date')

        if location_filter:
            queryset = queryset.filter(location=location_filter)
        
        if event_date_filter:
            queryset = queryset.filter(event_date=event_date_filter)
        else:
            queryset = queryset.upcoming_events()
        
        return queryset


def event_detail(request, event_id):
    """
    shows all the details of the event.
    """
    event = get_object_or_404(Event, id=event_id)
    is_attending = EventParticipant.is_attending(
        event, request.user)
    return render(request, 'events/event_detail.html', {
        'event': event, 'is_attending': is_attending})


@login_required
def event_form_view(request, event_id=None):
    """
    creates new event to add to the db and list
    in the event list.
    Allows to modify created event
    """
    if event_id:
        event = get_object_or_404(Event, id=event_id)
    else:
        event = None
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            if event_id is None:
                event.user = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
        else:
            return HttpResponse(
                "Form is invalid, check the fields")
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_form.html', {
        'form': form, 'event': event})


@login_required
def event_delete(request, event_id):
    """
    deletes an event if it's an event from the 
    current user
    """
    event_instance = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event_instance.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {
        'event': event_instance})


def create_location(request):
    """
    creates the location to add
    to the db
    """
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = LocationForm()
    
    return render(request, 'events/create_location.html', {
        'form': form})


@login_required
def add_participants(request, event_id):
    """
    Add participants and uses jsonresponse to
    communicate with the js file
    It also add the user to a db with the selected
    event to avoid multiple joins from a single user
    """
    if request.method == "POST":
        try:
            event = Event.objects.get(id=event_id)
            event.add_participants(request.user)
            return JsonResponse({
                'status': 'success', 'participants': event.participants})
        except Event.DoesNotExist:
            return JsonResponse({
                'status': 'fail', 'message': 'Event does not exist'})
    return JsonResponse({
        'status': 'fail', 'message': 'Invalid request'})


@login_required
def remove_participants(request, event_id):
    """
    Remove participants and uses jsonresponse to
    communicate with the js file
    It also remove the user from db with the selected
    event to avoid multiple leaves from a single user
    """
    if request.method == "POST":
        try:
            event = Event.objects.get(id=event_id)
            event.remove_participants(request.user)
            return JsonResponse({
                'status': 'success', 'participants': event.participants})
        except Event.DoesNotExist:
            return JsonResponse({
                'status': 'fail', 'message': 'Event does not exist'})
    return JsonResponse({
        'status': 'fail', 'message': 'Invalid request'})



