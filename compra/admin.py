from django.contrib import admin
from compra.models import Compra, DetalleCompra
from compra.forms import CompraForm, DetalleCompraForm

# Register your models here.

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    form = DetalleCompraForm
    extra = 5

class CompraAdmin(admin.ModelAdmin):
	inlines = (DetalleCompraInline,)
	form = CompraForm

	change_form_template = 'compra_form.html'

	list_display = ('numero_factura', 'fecha', 'proveedor', 'total')
	ordering = ('-fecha',)
	search_fields = ('numero_factura','fecha','proveedor__nombre')


admin.site.register(Compra, CompraAdmin)