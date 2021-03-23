from django import forms
from .models import squirrel_data

class SquirreldataForm(forms.ModelForm):
    class Meta:
        model = squirrel_data
        fields = '__all__'
