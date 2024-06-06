from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, LocationForm

# Create your views here.

class EventList(generic.ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = 'events'
    paginate_by = 6


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})


def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location_name = form.cleaned_data['location_name']
            # Create a new Location object with the provided name
            new_location = form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})