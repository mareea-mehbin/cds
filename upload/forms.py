from django import forms
from .models import UploadCriminal, States, Cities

class UploadCriminalForm(forms.ModelForm):
    class Meta:
        model = UploadCriminal
        fields = ['name', 'age', 'physical_description', 'date', 'state', 'city', 'crime_type', 'arresting_agency', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter your name", 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'placeholder': "Enter Criminal's age", 'class': 'form-control'})
        }