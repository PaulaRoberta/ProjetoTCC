from django.conf.urls import url
from app.controllers import (event, funcionamento, sumario, errosfrequentes,
                             equipamento, qrcode)

urlpatterns = [
    url(r'^event/create', event.create, name='index'),
    url(r'^equipamento/(?P<id>\d+)',equipamento.funcionamento, name='funcionamento'),
    url(r'^sumario/create',sumario.create, name='sumario'),
    url(r'^equipamento$',equipamento.index, name='equipamento'),
    url(r'^errosfrequentes/(?P<id>\d+)',errosfrequentes.show, name='errosfrequentes'),
    url(r'^equipamento/qrcode/(?P<id>\d+)', equipamento.get_qrcode, name='get qrcode'),
    url(r'^qrcode$', qrcode.reader, name="qrcode"),
    url(r'^funcionamento/(?P<id>\d+)',funcionamento.index, name='funcionamento')
]