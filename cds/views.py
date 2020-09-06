from django.shortcuts import render, redirect
from contactus.forms import ContactForm
from django.urls import reverse

def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print("hi")
        else:
            print('not')
    return render(request, 'home.html', {'contactForm': form})
