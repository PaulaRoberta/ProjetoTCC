from django.conf.urls import url
from app.controllers import event, funcionamento,sumario,errosfrequentes, equipamento

urlpatterns = [
    url(r'^event/create', event.create, name='index'),
    url(r'^funcionamento/create',funcionamento.create, name='funcionamento'),
    url(r'^sumario/create',sumario.create, name='sumario'),
    url(r'^equipamento$',equipamento.index, name='equipamento'),
    url(r'^errosfrequentes/(?P<id>\d+)',errosfrequentes.show, name='errosfrequentes'),
]