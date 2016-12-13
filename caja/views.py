from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from extra.globals import *

from django.contrib.auth.models import User
from caja.models import *
# Create your views here.

class AperturaCajaListView(ListView):
    model = AperturaCaja
    template_name = "aperturacaja_list.html"
    paginate_by = 30

    def get_queryset(self):
        aperturascajas = AperturaCaja.objects.all()

        usuario_id=self.request.GET.get('usuario_id','')
        if usuario_id !='':
            aperturascajas = aperturascajas.filter(usuario_id = usuario_id)

        return aperturascajas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AperturaCajaListView, self).get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()
        context['usuario_id'] = int(self.request.GET.get('usuario_id','')) if (self.request.GET.get('usuario_id','') != '') else ''
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(AperturaCajaListView, self).dispatch(*args, **kwargs)


class CierreCajaListView(ListView):
    model = CierreCaja
    template_name = "cierrecaja_list.html"
    paginate_by = 30

    def get_queryset(self):
        cierrescajas = CierreCaja.objects.all()

        usuario_id=self.request.GET.get('usuario_id','')
        if usuario_id !='':
            cierrescajas = cierrescajas.filter(usuario_id = usuario_id)

        return cierrescajas.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CierreCajaListView, self).get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()
        context['usuario_id'] = int(self.request.GET.get('usuario_id','')) if (self.request.GET.get('usuario_id','') != '') else ''
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CierreCajaListView, self).dispatch(*args, **kwargs)


def caja_presentacion(request):
    context = RequestContext(request)
    titulo="CAJA"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)