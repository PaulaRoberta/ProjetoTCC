from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Entity,Midias

def create(request):
    midias = Midias.objects.all()
    entitys = Entity.objects.all()
    return render(request, 'funcionamento/form_create.html', {
        "midias": midias,
        "entitys": entitys
    })

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass