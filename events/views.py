from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
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

    return render(request, 'events/event_form.html', {'form': form, 'event': event})

# deletes an event if it's an event from the current user 
# (this passage is controlled in the modify part that leads to the possibility to delete)
@login_required
def event_delete(request, event_id):
    event_instance = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event_instance.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event_instance})

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


# add participants and uses jsonresponse as I utilized js to update the db
# without needing to load the user to another page
# they can be further improved adding the user.id check to let every
# user join only once and, when joined, leave
@login_required
def add_participants(request, event_id):
    if request.method == "POST":
        try:
            event = Event.objects.get(id=event_id)
            event.add_participants()
            return JsonResponse({'status': 'success', 'participants': event.participants})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Event does not exist'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'})


@login_required
def remove_participants(request, event_id):
    if request.method == "POST":
        try:
            event = Event.objects.get(id=event_id)
            event.remove_participants()
            return JsonResponse({'status': 'success', 'participants': event.participants})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Event does not exist'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'})

        


# creates the view to see the details of the event clicked
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})


