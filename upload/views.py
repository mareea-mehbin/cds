from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def upload_entry(request):
    return render(request, 'upload/upload_form.html')
