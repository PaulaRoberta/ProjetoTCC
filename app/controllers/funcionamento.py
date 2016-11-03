from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Entity,Midias

def partfuncionamento(request, id):
    my_entity = Entity.objects.get(pk=id)
    midias = Midias.objects.all()
    return render(request, 'funcionamento/partfuncionamento.html', {
        "entity": my_entity,
        "midias": midias
    })

def index(request, id):
    my_entity = Entity.objects.get(pk=id)
    midias = Midias.objects.all()
    return render(request, 'funcionamento/index.html', {
        "entity": my_entity,
        "midias": midias
    })

