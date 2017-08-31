from django.conf.urls import patterns, include, url
from producto.views import *
from producto.autocomplete import *
from producto.ajax import *


urlpatterns = [
    url(
        'productoautocomplete/$',
        ProductoAutocomplete.as_view(),
        name='producto-autocomplete',
    ),

    url(r'^getprecioventa/$',get_precioventa),
    url('getlistapreciosventa/$',get_listapreciosventa),

    url(r'^getpreciocompra/$',get_preciocompra),
    url('getlistaprecioscompra/$',get_listaprecioscompra),

    url(r'^categoria/$', CategoriaListView.as_view(),name='categoria_lis'),
    url(r'^insercioninmediata/$', InsercionInmediataListView.as_view(),name='insercioninmeadiata_lis'),
    url(r'^sustraccioninmediata/$', SustraccionInmediataListView.as_view(),name='sustraccioninmeadiata_lis'),

    url(r'^unidadmedida/$', UnidadMedidaListView.as_view(),name='unidadmedida_lis'),

    url(r'^producto/$', ProductoListView.as_view(),name='producto_lis'),

    url(r'^corrompidos/$', listar_corrompidos),

    url(r'^$', producto_presentacion),

]