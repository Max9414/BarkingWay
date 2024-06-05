from django import forms
from .models import Owner, Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog

        #fields to exclude
        exclude = ["owner"]

        #widgets to create a new dog data in th db
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bitten': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'vaccinated': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'rough': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Dog Name',
            'breed': 'Breed',
            'age': 'Age',
            'bitten': "Bitten Dog",
            'vaccinated': "Vaccinated Dog",
            'rough': "Rough player",
        }