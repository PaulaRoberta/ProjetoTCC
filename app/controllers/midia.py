from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def index(request):
    form = UploadFileForm()
    return render(request, 'midia/index.html', {'form': form})

def upload_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect('/success/url/')
