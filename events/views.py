from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Event
from .forms import EventForm, LocationForm

# Create your views here.

class EventList(generic.ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = 'events'
    paginate_by = 6


# shows all the details of the event
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})


# creates new event to add to the db and list in the event list
# it also allows the user to modify the created event while the fields get autopopulated with
# the original event details
@login_required
def event_form_view(request, event_id=None):
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
            return HttpResponse("Form is invalid, check the fields")
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_form.html', {'form': form})

# creates the new location to add to the db
def create_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_form_view')
    else:
        form = LocationForm()
    
    return render(request, 'events/create_location.html', {'form': form})


# creates the view to see the details of the event clicked
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})


