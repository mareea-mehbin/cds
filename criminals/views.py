from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Criminal

# Create your views here.
def search(request):
    if request.GET.get('search'):
        criminals = Criminal.objects.filter(name=request.GET.get('search'))
    else:
        criminals = Criminal.objects.all()

    paginator = Paginator(criminals, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'criminals/criminal_view.html', {'criminals': page_obj})