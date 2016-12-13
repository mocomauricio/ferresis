from django.conf.urls import patterns, include, url
from compra.views import *

urlpatterns = [

    url(r'^compra/(?P<pk>\d+)/detail/$', CompraDetailView.as_view(), name='compra_det'),
    url(r'^compra/$', CompraListView.as_view(), name='compra_lis'),
    url(r'^$', compra_presentacion),

]