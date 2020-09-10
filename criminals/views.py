from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Criminal
from .forms import AdvancedSearch
from django.views import View
from django.views.generic.detail import DetailView

class CriminalsView(View):
    def get(self, request):
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

        return render(request, 'criminals/criminals.html', {'criminals': page_obj, 'advancedSearch': form})

class CriminalDetailView(DetailView):
    model = Criminal

    def get(self, request, pk):
        criminal = self.model.objects.get(pk=pk)
        return render(request, 'criminals/criminal_detail.html', {'criminal': criminal})