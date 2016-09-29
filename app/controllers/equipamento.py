from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from app.models import Entity

def index(request):
    entitys = Entity.objects.all()
    return render(request, 'equipamento/index.html', {
        "entitys": entitys
    })