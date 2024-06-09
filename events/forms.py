from django import forms
from .models import Event, Location
from django.core.exceptions import ValidationError
from django.utils import timezone


class EventForm(forms.ModelForm):
    """
    override the timefield input in the model with a dropdown menu
    also override the datefield to input the date from a menu
    """

    class Meta:
        model = Event
        fields = [
            'event', 'location', 'event_date', 'description', 'start_time', 'end_time']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        event_date = cleaned_data.get('event_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Check for valid time
        if start_time and end_time and end_time < start_time:
            raise ValidationError(
                "End time can't be earlier than start time")

        # Check for date to be later than the day of creation
        if event_date <= timezone.now().date():
            raise ValidationError(
                "Event date cannot be today or in the past. Please select a future date.")

        return cleaned_data


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['location']
    
    def clean_location(self):
        location = self.cleaned_data['location']
        # Check if a location with the same name already exists
        if Location.objects.filter(location__iexact=location).exists():
            raise forms.ValidationError(
                "A location with this name already exists.")
        return location