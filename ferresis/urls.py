"""ferresis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/auth/', include("sistema.urls", namespace="cliente")),
    url(r'^admin/sistema/', include("sistema.urls", namespace="cliente")),

    url(r'^admin/caja/', include("caja.urls", namespace="cliente")),

    url(r'^admin/cliente/', include("cliente.urls", namespace="cliente")),
    url(r'^admin/proveedor/', include("proveedor.urls", namespace="proveedor")),
    url(r'^admin/producto/', include("producto.urls", namespace="producto")),
    url(r'^admin/presupuesto/', include("presupuesto.urls", namespace="presupuesto")),
    url(r'^admin/venta/', include("venta.urls", namespace="venta")),
    url(r'^admin/compra/', include("compra.urls", namespace="compra")),


    url(r'^admin/', admin.site.urls),

    url(r'^chaining/', include('smart_selects.urls')),
]
