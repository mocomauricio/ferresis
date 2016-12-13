from django.shortcuts import render
from dal import autocomplete
from django.db.models import Q
from producto.models import *
# Create your views here.

class ProductoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Producto.objects.none()

        qs = Producto.objects.all()

        if self.q:
            qs = qs.filter( Q(nombre__istartswith=self.q) | Q(codigo__istartswith=self.q) )

        return qs

