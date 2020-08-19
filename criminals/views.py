from django.shortcuts import render
from .models import Criminal
from django.http import HttpResponse

# Create your views here.
def display(request):
    criminals = Criminal.objects.all()
    return render(request, 'criminals/criminal_card.html', {'criminals': criminals})

def search(request):
    criminals = Criminal.objects.filter(name=request.GET.get('search'))
    return render(request, 'criminals/search.html', {'criminals': criminals})