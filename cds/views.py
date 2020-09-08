from django.shortcuts import render, redirect
from contactus.forms import ContactForm
from django.urls import reverse

def home(request):
    return render(request, 'home.html')
