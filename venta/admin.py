from django.contrib import admin
from venta.models import Venta, DetalleVenta
from venta.forms import VentaForm, DetalleVentaForm

# Register your models here.

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	form = DetalleVentaForm
	extra = 5

class VentaAdmin(admin.ModelAdmin):
	inlines = (DetalleVentaInline,)
	form = VentaForm

	change_form_template = 'venta_form.html'

	list_display = ('numero_factura', 'fecha', 'cliente', 'total')
	ordering = ('-fecha',)
	search_fields = ('numero_factura','fecha','cliente__nombre')


	def response_add(self, request, obj, post_url_continue=None):
		res = super(VentaAdmin, self).response_add(request, obj,post_url_continue)
		if "next" in request.GET:
			return HttpResponseRedirect(request.GET['next'])
		else:
			return res
			
			
	def response_change(self, request, obj):
		res = super(VentaAdmin, self).response_change(request, obj)
		if "next" in request.GET:
			return HttpResponseRedirect(request.GET['next'])
		else:
			return res


	def response_delete(self,request, obj_display, obj_id):
		res = super(VentaAdmin, self).response_delete(request, obj_display, obj_id)
		if "next" in request.GET:
			return HttpResponseRedirect(request.GET['next'])
		else:
			return res

admin.site.register(Venta, VentaAdmin)