from django.shortcuts import render
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from presupuesto.models import Presupuesto

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
# Create your views here.


class PresupuestoListView(ListView):
    model = Presupuesto
    paginate_by = 30
    template_name = "admin/presupuesto/presupuesto/presupuesto_list.html"

    def get_queryset(self):
        q=self.request.GET.get('q','')
        return Presupuesto.objects.filter( Q(cliente__nombre__istartswith=q) | Q(cliente__ruc__istartswith=q)).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(PresupuestoListView, self).get_context_data(**kwargs)

        context['q']=self.request.GET.get('q','')        
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(PresupuestoListView, self).dispatch(*args, **kwargs)
