from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Location,Entity

def reader(request):
    return render(request, 'qrcode-reader/index.html')

def create(request):
    return render(request, 'qrcode-reader/index.html')
