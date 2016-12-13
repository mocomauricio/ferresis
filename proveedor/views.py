from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from proveedor.models import *
from extra.globals import *

# Create your views here.


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor_list.html"
    paginate_by = 30

    def get_queryset(self):
        proveedores = Proveedor.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            proveedores = proveedores.filter( Q(nombre__icontains=q) | Q(ruc__startswith=q) )

        return proveedores.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ProveedorListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''): 

            lista_datos=[]
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.nombre,
                    dato.ruc,
                    dato.direccion,
                    dato.telefono,
                    dato.celular,
                    dato.email,
                ])

            titulos=[ 'Nombre', 'RUC', 'Direccion', 'Telefono', 'Celular', 'Email' ]
            return listview_to_excel(lista_datos,'Proveedores',titulos)
        
        return super(ProveedorListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ProveedorListView, self).dispatch(*args, **kwargs)

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor_detail.html"


def proveedor_presentacion(request):
    context = RequestContext(request)
    titulo="PROVEEDORES"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)
