from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm

# Create your views here.
@login_required(login_url='/accounts/login')
def upload_entry(request):
    if request.method =='GET':
        form = UploadCriminalForm()
    else:
        form = UploadCriminalForm(request.POST)
        if form.is_valid():
            new_upload = form.save()
            return redirect('upload:upload')
    return render(request, 'upload/upload_form.html', {'uploadForm': form})

