from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    if (request.method == 'POST'):
        form = ContactForm(request.get.POST)
    else:
        form = ContactForm()
    return render(request, 'contactus/contact.html', {'contactForm': form})