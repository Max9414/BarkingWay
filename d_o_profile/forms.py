from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Owner, Dog, Breed

AGE_CHOICES = [(i, str(i)) for i in range(1, 21)]

# Form designed for managing Dog model instances, utilizing the crispy-forms library to enhance its layout and usability.
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


    def get_form_layout(self):
        return Layout(
            'name',
            'breed',
            'age',
            'bitten',
            'vaccinated',
            'rough',
        )


# Form designed for managing Owner model instances, utilizing the crispy-forms library to enhance its layout and usability.
class OwnerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Owner
        exclude = ["name"]
        labels = {
            'image': 'image',
            'displayname': 'display name',
            'info': "info",
        }

    def get_form_layout(self):
        return Layout(
            'name',
            'image',
            'displayname',
            'info',
        )