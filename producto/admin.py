from django.contrib import admin
from producto.models import UnidadMedida, Categoria, Producto, PrecioCompraProducto, PrecioVentaProducto, InsercionInmediata, SustraccionInmediata
from venta.models import DetalleVenta
from compra.models import DetalleCompra
from producto.models import *
from producto.forms import *
# Register your models here.


class UnidadMedidaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'abreviatura', )
	ordering = ('nombre',)
	search_fields = ('nombre','abreviatura')

admin.site.register(UnidadMedida, UnidadMedidaAdmin)


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	ordering = ('nombre',)
	search_fields = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)


class PrecioCompraProductoInline(admin.TabularInline):
	model = PrecioCompraProducto
	form = PrecioCompraProductoForm
	extra = 4

class PrecioVentaProductoInline(admin.TabularInline):
	model = PrecioVentaProducto
	form = PrecioVentaProductoForm
	extra = 4

class ProductoAdmin(admin.ModelAdmin):
	inlines = (PrecioCompraProductoInline, PrecioVentaProductoInline,)
	change_form_template = 'producto_form.html'

	form = ProductoForm

	list_display = ('codigo','nombre','get_cantidad', )
	ordering = ('codigo','nombre',)
	search_fields = ('codigo','nombre')
	
	filter_horizontal = ('proveedor',)

	fieldsets = (
		(None, {
			'fields': [
				('codigo', 'nombre'), 
				('categoria', 'unidad_medida'),
				'proveedor'
			]
		}),

		('PRECIOS PRINCIPALES', {
			'fields': ['iva','precio_compra', 'precio_venta']
		}),
	)

admin.site.register(Producto, ProductoAdmin)


class InsercionInmediataAdmin(admin.ModelAdmin):
	form = InsercionInmediataForm
	list_display = ('producto', 'cantidad', 'observacion', 'fecha_hora', )
	ordering = ('-fecha_hora',)
	search_fields = ('producto.codigo','producto.nombre', 'observacion',)

admin.site.register(InsercionInmediata, InsercionInmediataAdmin)

class SustraccionInmediataAdmin(admin.ModelAdmin):
	form = SustraccionInmediataForm
	list_display = ('producto', 'cantidad', 'observacion', 'fecha_hora', )
	ordering = ('-fecha_hora',)
	search_fields = ('producto.codigo','producto.nombre', 'observacion',)

admin.site.register(SustraccionInmediata, SustraccionInmediataAdmin)

