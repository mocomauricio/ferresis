from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from cliente.models import *
from venta.models import *

class VentaDetailView(DetailView):
    model = Venta
    template_name = "venta_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VentaDetailView, self).get_context_data(**kwargs)
        context['detalles'] = DetalleVenta.objects.filter(venta_id=self.object.id)
        return context


class VentaListView(ListView):
    model = Venta
    template_name = "venta_list.html"
    paginate_by = 30

    def get_queryset(self):
        ventas = Venta.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            ventas = ventas.filter(numero_factura=q)

        cliente_id = self.request.GET.get('cliente_id', '')
        if cliente_id != '':
            ventas = ventas.filter(cliente_id=cliente_id)


        return ventas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(VentaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['clientes'] = Cliente.objects.all()
        context['cliente_id'] = int(self.request.GET.get('cliente_id', '')) if (self.request.GET.get('cliente_id', '') != '') else ''
        return context


def venta_presentacion(request):
    context = RequestContext(request)
    titulo = "VENTAS"
    descripcion = "."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)