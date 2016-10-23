from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Entity,Midias


def index(request, id):
    midias = Midias.objects.all()
    entity = Entity.objects.get(pk=id)
    return render(request, 'funcionamento/form_create.html', {
        "midias": midias,
        "entity": entity
    })

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass