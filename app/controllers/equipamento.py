from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests.utils import quote

from app.models import Entity

def funcionamento(request, id):
    entity = Entity.objects.get(pk=id)
    return render(request, 'funcionamento/form_create.html', {
        "entity": entity
    })

def index(request):
    entitys = Entity.objects.all()
    return render(request, 'equipamento/index.html', {
        "entitys": entitys
    })

def get_qrcode(request, id):
    path = quote('/funcionamento/%s' % id, safe='')
    url = 'https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=%s' % path

    return HttpResponse(url);
