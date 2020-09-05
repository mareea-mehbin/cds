from django import forms
from contactus.models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']