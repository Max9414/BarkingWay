from django import forms
from .models import Event, Location
from django.core.exceptions import ValidationError


#override the timefield input in the model with a dropdown menu
#also override the datefield to input the date from a menu
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event', 'location', 'event_date', 'description', 'start_time', 'end_time']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }



    #also, if the start time is after end time, it will raise an error and ask input again
    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        add_location = cleaned_data.get('add_location')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Check for custom location
        if location and location.location == 'Other' and add_location:
            Location.objects.create(location=add_location)
            cleaned_data['location'] = add_location

        # Check for valid time
        if start_time and end_time and end_time < start_time:
            raise ValidationError("End time can't be earlier than start time")

        return cleaned_data


class LocationForm(forms.ModelForm):
    location_name = forms.CharField(max_length=200, label="Location Name")

    class Meta:
        model = Location
        fields = ['location_name']
    
    def clean_location_name(self):
        location_name = self.cleaned_data['location_name']
        # Check if a location with the same name already exists
        if Location.objects.filter(location_name__iexact=location_name).exists():
            raise forms.ValidationError("A location with this name already exists.")
        return location_name
