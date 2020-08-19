from django.shortcuts import render
from .models import Criminal
from django.http import HttpResponse

# Create your views here.
def search(request):
    if request.GET.get('search'):
        criminals = Criminal.objects.filter(name=request.GET.get('search'))
    else:
        criminals = Criminal.objects.all()
    return render(request, 'criminals/criminal_view.html', {'criminals': criminals})