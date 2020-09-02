from django import forms
from .models import UploadCriminal, States, Cities

class UploadCriminalForm(forms.ModelForm):
    class Meta:
        model = UploadCriminal
        fields = ['name', 'age', 'physical_description', 'date', 'state', 'city', 'crime_type', 'arresting_agency', 'photo']