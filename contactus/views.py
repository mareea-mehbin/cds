from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    return render(request, 'contactus/contact.html', {'contactForm': form})