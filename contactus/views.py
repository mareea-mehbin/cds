from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contactus/contact.html'
    form_class = ContactForm
    success_url = 'success/'
    success_message = "Submitted, Thank You !"

    def form_valid(self, form):
        new_message = form.save()
        return super().form_valid(form)

def success(request):
    return render(request, 'contactus/success.html')