from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Criminal
from .forms import AdvancedSearch
from django.views import View
from django.views.generic import DetailView, ListView

class CriminalsView(ListView):
    template_name = 'criminals/criminals.html'
    form_class = AdvancedSearch
    model = Criminal
    context_object_name = 'criminals'

    def get_queryset(self):
        name = self.kwargs.get('name', None)

        form = self.form_class(self.request.GET)

        if form.is_valid():
            return self.model.objects.filter(name__contains=form.cleaned_data['name'])
        return self.model.objects.all()

    def get(self, request):
        form = AdvancedSearch()
        criminals = Criminal.objects.all()

    """ def get(self, request):
        # If advanced search
        if (request.GET.get('name')):
                form = AdvancedSearch(request.GET)
                if (form.is_valid()):
                    criminals = Criminal.objects.filter(name__contains=form.cleaned_data['name'])
                else:
                    criminals = Criminal.objects.all()
        # If default view
        else:
            form = AdvancedSearch()
            criminals = Criminal.objects.all()
        
        # Pagination
        paginator = Paginator(criminals, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'criminals/criminals.html', {'criminals': page_obj, 'advancedSearch': form}) """

class CriminalDetailView(DetailView):
    model = Criminal
    template_name = 'criminals/criminal_detail.html'