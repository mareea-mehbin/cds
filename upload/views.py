from django.shortcuts import render

# Create your views here.
def upload_entry(request):
    return render(request, 'upload/upload_form.html')
