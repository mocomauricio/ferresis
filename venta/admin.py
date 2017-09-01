from django.contrib import admin
from venta.models import Venta, DetalleVenta
from venta.forms import VentaForm, DetalleVentaForm

# Register your models here.

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	form = DetalleVentaForm
	extra = 5

	fieldsets = (
		(None, {
			'fields': [('producto', 'cantidad', 'precio', 'precio_unitario', 'subtotal')]
		}),
	)

class VentaAdmin(admin.ModelAdmin):
	inlines = (DetalleVentaInline,)
	form = VentaForm

	change_form_template = 'venta_form.html'

	list_display = ('numero_factura', 'fecha', 'cliente', 'total')
	ordering = ('-fecha',)
	search_fields = ('numero_factura','fecha','cliente__nombre')


admin.site.register(Venta, VentaAdmin)
