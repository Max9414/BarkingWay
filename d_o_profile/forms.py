from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Owner, Dog, Breed

AGE_CHOICES = [(i, str(i)) for i in range(1, 21)]

# class DogForm(forms.ModelForm):
#     class Meta:
#         model = Dog

#         #fields to exclude
#         exclude = ["owner"]

#         #widgets to create a new dog data in th db
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'breed': forms.Select(attrs={'class': 'form-control'}),
#             'age': forms.Select(choices=AGE_CHOICES, attrs={'class': 'form-control'}),
#             'bitten': forms.CheckboxInput(attrs={'class': 'form-control'}),
#             'vaccinated': forms.CheckboxInput(attrs={'class': 'form-control'}),
#             'rough': forms.CheckboxInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'name': 'Dog Name',
#             'breed': 'Breed',
#             'age': 'Age',
#             'bitten': "Bitten Dog",
#             'vaccinated': "Vaccinated Dog",
#             'rough': "Rough player",
#         }
#     breed = forms.ModelChoiceField(queryset=Breed.objects.all())


class DogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Dog
        exclude = ["owner"]
        labels = {
            'name': 'Dog Name',
            'breed': 'Breed',
            'age': 'Age',
            'bitten': "Bitten Dog",
            'vaccinated': "Vaccinated Dog",
            'rough': "Rough player",
        }

    # Override the 'breed' field to use a ModelChoiceField
    breed = forms.ModelChoiceField(queryset=Breed.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def get_form_layout(self):
        return Layout(
            'name',
            'breed',
            'age',
            'bitten',
            'vaccinated',
            'rough',
        )