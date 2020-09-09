from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadCriminalForm
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class UploadView(View):
    def get(self, request):
        form = UploadCriminalForm()
        return render(request, 'upload/upload_form.html', {'uploadForm': form})

    def post(self, request):
        form = UploadCriminalForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_upload = form.save()
            return redirect('upload:upload')
        return render(request, 'upload/upload_form.html', {'uploadForm': form})

