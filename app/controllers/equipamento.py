from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests.utils import quote

from app.models import Entity, Midias

def view(request, id):
    entity = Entity.objects.get(pk=id)
    return render(request, 'equipamento/view.html', {
        "entity": entity
    })

def index(request):
    entitys = Entity.objects.all()
    return render(request, 'equipamento/index.html', {
        "entitys": entitys
    })

def get_qrcode(request, id):
    path = quote('/equipamento/%s' % id, safe='')
    url = 'https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=%s' % path

    return HttpResponse(url);
