from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm

# Create your views here.
@login_required(login_url='/accounts/login')
def upload_entry(request):
    form = UploadCriminalForm()
    return render(request, 'upload/upload_form.html', {'uploadForm': form})
