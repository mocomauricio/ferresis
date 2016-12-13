from django.conf.urls import patterns, include, url

from caja.views import *

urlpatterns = [

    url(r'^aperturacaja/$', AperturaCajaListView.as_view(), name='aperturacaja_lis'),
    url(r'^cierrecaja/$', CierreCajaListView.as_view(), name='cierrecaja_lis'),

    url(r'^$', caja_presentacion),
]
