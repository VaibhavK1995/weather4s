from django.forms import ModelForm, TextInput
from .models import location


class CityForm(ModelForm):
    class Meta:
        model = location
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
