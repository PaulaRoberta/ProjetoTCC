from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Location,Entity

def create(request):
    locations = Location.objects.all()
    entitys = Entity.objects.all()
    return render(request, 'event/form_create.html', {
        "locations": locations,
        "entitys": entitys
    })

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass

