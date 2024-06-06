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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.all()
        self.fields['custom_location'] = forms.CharField(max_length=200, required=False)

    #if the selected location is other, allows the user to create the new location name
    #also, if the start time is after end time, it will raise an error and ask input again
    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        custom_location = cleaned_data.get('custom_location')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Check for custom location
        if location and location.location == 'Other' and custom_location:
            cleaned_data['location'] = Location.objects.create(location=custom_location)

        # Check for valid time
        if start_time and end_time and end_time < start_time:
            raise ValidationError("End time can't be earlier than start time")

        return cleaned_data