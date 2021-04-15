from django import forms
from .models import squirrel_data

class SquirreldataForm(forms.ModelForm):
    '''
    Class to handle ModelForms that are used in the Add Sighting form
    '''
    class Meta:
        model = squirrel_data
        fields = '__all__'
