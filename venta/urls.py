from django.conf.urls import patterns, include, url
from venta.views import *

urlpatterns = [

    url(r'^venta/(?P<pk>\d+)/detail/$', VentaDetailView.as_view(), name='venta_det'),
    url(r'^venta/$', VentaListView.as_view(), name='venta_lis'),
    url(r'^$', venta_presentacion),

]