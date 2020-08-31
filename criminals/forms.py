from django import forms

class AdvancedSearch(forms.Form):
    name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=12, required=False)