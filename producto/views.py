from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from dal import autocomplete
from django.db.models import Q
from producto.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from extra.globals import *

# Create your views here.

class ProductoListView(ListView):
    model = Producto
    paginate_by = 30
    template_name = "producto_list.html"

    def get_queryset(self):
        q=self.request.GET.get('q','')
        return Producto.objects.filter( Q(codigo__istartswith=q) | Q(nombre__icontains=q)).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ProductoListView, self).get_context_data(**kwargs)
        context['q']=self.request.GET.get('q','')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''): 
           
            lista_datos=[]
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([dato.codigo, 
                                    dato.nombre,
                                    separador_de_miles(dato.get_cantidad()),
                                    separador_de_miles(dato.get_precio_compra()),
                                    separador_de_miles(dato.get_precio_venta())
                                    ])
           
            titulos=['Codigo','Nombre','Cantidad','Precio de compra','Precio de venta']
            return listview_to_excel(lista_datos,'Producto',titulos)
        else:
            return super(ProductoListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductoListView, self).dispatch(*args, **kwargs)


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria_list.html"
    paginate_by = 30

    def get_queryset(self):
        categorias = Categoria.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            categorias = categorias.filter( nombre__icontains=q )

        return categorias.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaListView, self).dispatch(*args, **kwargs)

class UnidadMedidaListView(ListView):
    model = UnidadMedida
    template_name = "unidadmedida_list.html"
    paginate_by = 30

    def get_queryset(self):
        unidadesmedidas = UnidadMedida.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            unidadesmedidas = unidadesmedidas.filter( nombre__icontains=q )

        return unidadesmedidas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UnidadMedidaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(UnidadMedidaListView, self).dispatch(*args, **kwargs)


class InsercionInmediataListView(ListView):
    model = InsercionInmediata
    template_name = "insercioninmediata_list.html"
    paginate_by = 30

    def get_queryset(self):
        insercionesinmediatas = InsercionInmediata.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            insercionesinmediatas = insercionesinmediatas.filter( Q(producto__nombre__icontains=q) | Q(producto__codigo__istartswith=q) )

        return insercionesinmediatas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(InsercionInmediataListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(InsercionInmediataListView, self).dispatch(*args, **kwargs)


class SustraccionInmediataListView(ListView):
    model = SustraccionInmediata
    template_name = "sustraccioninmediata_list.html"
    paginate_by = 30

    def get_queryset(self):
        sustraccionesinmediatas = SustraccionInmediata.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            sustraccionesinmediatas = sustraccionesinmediatas.filter( Q(producto__nombre__icontains=q) | Q(producto__codigo__istartswith=q) )

        return sustraccionesinmediatas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SustraccionInmediataListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(SustraccionInmediataListView, self).dispatch(*args, **kwargs)

def producto_presentacion(request):
    context = RequestContext(request)
    titulo="PRODUCTOS"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)


