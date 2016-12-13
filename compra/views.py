from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from proveedor.models import *
from compra.models import *

class CompraDetailView(DetailView):
    model = Compra
    template_name = "compra_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CompraDetailView, self).get_context_data(**kwargs)
        context['detalles'] = DetalleCompra.objects.filter(compra_id=self.object.id)
        return context


class CompraListView(ListView):
    model = Compra
    template_name = "compra_list.html"
    paginate_by = 30

    def get_queryset(self):
        compras = Compra.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            compras = compras.filter(numero_factura=q)

        proveedor_id = self.request.GET.get('proveedor_id', '')
        if proveedor_id != '':
            compras = compras.filter(proveedor_id=proveedor_id)


        return compras.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CompraListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['proveedores'] = Proveedor.objects.all()
        context['proveedor_id'] = int(self.request.GET.get('proveedor_id', '')) if (self.request.GET.get('proveedor_id', '') != '') else ''
        return context


def compra_presentacion(request):
    context = RequestContext(request)
    titulo = "VENTAS"
    descripcion = "."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)