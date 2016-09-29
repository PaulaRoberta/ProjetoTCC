from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Entity,Midias,Comment, FAQ

def index(request):
    entitys = Entity.objects.all()
    return render(request, 'errosfrequentes/index.html', {
        "entitys": entitys
    })

def show(request, id):
    my_entity = Entity.objects.get(pk=id)
    faqs = FAQ.objects.filter(entity=my_entity).all()
    return render(request, 'errosfrequentes/show.html', {
        "entity": my_entity,
        "faqs": faqs
    })