from django.contrib import admin
from caja.models import AperturaCaja, CierreCaja
from caja.forms import *

# Register your models here.


class AperturaCajaAdmin(admin.ModelAdmin):
	form = AperturaCajaForm
	list_display = ('usuario', 'monto', 'fecha_hora',)
	ordering = ('-fecha_hora',)
	search_fields = ('usuario',)

admin.site.register(AperturaCaja, AperturaCajaAdmin)


class CierreCajaAdmin(admin.ModelAdmin):
	form = CierreCajaForm
	list_display = ('usuario', 'monto', 'fecha_hora',)
	ordering = ('-fecha_hora',)
	search_fields = ('usuario',)

admin.site.register(CierreCaja, CierreCajaAdmin)