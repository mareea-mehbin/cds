from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.views import View
from django.contrib import messages

# Create your views here.
class ContactFormView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contactus/contact.html', {'contactForm': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if (form.is_valid()):
            new_message = form.save()
            messages.success(request, 'Thank you for contacting us ! We will be with you shortly')
            return redirect('contactus:success')
        else:
            return render(request, 'contactus/contact.html', {'contactForm': form})

def success(request):
    return render(request, 'contactus/success.html')