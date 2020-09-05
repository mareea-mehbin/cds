from django.shortcuts import render
from contactus.forms import ContactForm

def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.get.POST)
    return render(request, 'home.html', {'contactForm': form})
