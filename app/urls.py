from django.conf.urls import url
from app.controllers import (event, funcionamento, sumario, errosfrequentes,
                             equipamento, qrcode, user)

urlpatterns = [
    url(r'^event/create', event.create, name='index'),

    url(r'^equipamento$',equipamento.index, name='equipamento'),
    url(r'^equipamento/(?P<id>\d+)',equipamento.view, name='equipamento'),
    url(r'^equipamento/qrcode/(?P<id>\d+)', equipamento.get_qrcode, name='get qrcode'),

    url(r'^funcionamento/(?P<id>\d+)',funcionamento.index, name='funcionamento'),
    url(r'^funcionamento/verificacao/(?P<id>\d+)',funcionamento.partfuncionamento, name='funcionamento'),

    url(r'^qrcode$', qrcode.reader, name="qrcode"),

    url(r'^errosfrequentes/(?P<id>\d+)',errosfrequentes.show, name='errosfrequentes'),

    url(r'^sumario/create',sumario.create, name='sumario'), #olhar n tem nada.

    url(r'^login$', user.login, name='login'),
    url(r'^do_login$', user.do_login, name='do login'),
    url(r'^user/create$', user.create, name='create'),
    url(r'^user/do_create$', user.do_create, name='do create'),

]