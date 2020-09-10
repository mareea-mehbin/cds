from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name *', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email *', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone *', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message *', 'rows': '8'})
        }