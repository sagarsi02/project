from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

from django.views.generic import TemplateView


def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['file']
        get_file_name = upload_file.name
        if get_file_name.endswith('.csv'):
            fs = FileSystemStorage()
            fs.save(upload_file.name, upload_file)
            messages.success(request, 'Successfully file uploded')
            return redirect('/')
        else:
            messages.success(request, 'Only .csv files are allowed')
            return render(request, 'upload.html')
    return render(request, 'upload.html')