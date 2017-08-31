from __future__ import unicode_literals

from django.db import models
from proveedor.models import Proveedor

from venta.models import *
from compra.models import *

from extra.globals import *

# Create your models here.
class UnidadMedida(models.Model):
	nombre = models.CharField(max_length=50,unique=True)
	abreviatura = models.CharField(max_length=10,unique=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Unidad de medida'
		verbose_name_plural = 'Unidades de medida'


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

IVA = (('IVA10', 'IVA 10%'), ('IVA5', 'IVA 5%'), ('EXENTA', 'EXENTA'))

class Producto(models.Model):
	codigo = models.CharField(max_length=50,unique=True)
	nombre = models.CharField(max_length=200,unique=True)
	categoria = models.ForeignKey(Categoria)
	unidad_medida = models.ForeignKey(UnidadMedida)
	iva = models.CharField("IVA",max_length=10, choices=IVA, default='IVA10')

	proveedor = models.ManyToManyField(Proveedor, blank=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		permissions = (
			("view_producto", "Puede ver la lista de productos"),
		)
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

	def get_cantidad(self):

		vendidos = DetalleVenta.objects.filter(producto_id = self.id)
		cantidad_vendida = 0
		print self.id
		precio_venta = PrecioVentaProducto.objects.filter(producto_id = self.id)
		precio_venta = precio_venta[0]


		print "111111"

		for vendido in vendidos:
			if vendido.precio == precio_venta:
				cantidad_vendida = cantidad_vendida + vendido.cantidad
			else:
				cantidad_vendida = cantidad_vendida + (vendido.cantidad*vendido.precio.factor_conversion)


		comprados = DetalleCompra.objects.filter(producto_id = self.id, compra__carga_inicial=True)
		cantidad_comprada = 0
		precio_compra = PrecioCompraProducto.objects.filter(producto_id = self.id)[0]
		for comprado in comprados:
			if comprado.precio == precio_compra:
				cantidad_comprada = cantidad_comprada + comprado.cantidad
			else:
				cantidad_comprada = cantidad_comprada + (comprado.cantidad*comprado.precio.factor_conversion)

		insertados = InsercionInmediata.objects.filter(producto_id = self.id)
		cantidad_insertada = 0
		for insertado in insertados:
			cantidad_insertada = cantidad_insertada + insertado.cantidad

		sustraidos = SustraccionInmediata.objects.filter(producto_id = self.id)
		cantidad_sustraida = 0
		for sustraido in sustraidos:
			cantidad_sustraida = cantidad_sustraida + sustraido.cantidad

		stock = cantidad_comprada + cantidad_insertada - cantidad_vendida - cantidad_sustraida

		return stock


	def get_precio_venta(self):
		return (PrecioVentaProducto.objects.filter(producto_id = self.id)[0]).precio_venta

	def get_precio_compra(self):
		return (PrecioCompraProducto.objects.filter(producto_id = self.id)[0]).precio_compra
	

class PrecioVentaProducto(models.Model):
	class Meta:
		verbose_name = 'Otro precio de venta'
		verbose_name_plural = 'Otros precios de venta'

	producto = models.ForeignKey(Producto)
	unidad_medida = models.ForeignKey(UnidadMedida)

	precio_venta = models.DecimalField("Precio de venta", max_digits=15,decimal_places=2)
	factor_conversion = models.DecimalField("Factor de conversion", max_digits=15,decimal_places=2, help_text="Numero a multiplicar para convertir en la unidad de medida principal")

	def __unicode__(self):
		return self.unidad_medida.abreviatura 

	def __str__(self):
		return separador_de_miles(self.precio_venta) + " Gs/" + self.unidad_medida.abreviatura 




class PrecioCompraProducto(models.Model):
	class Meta:
		verbose_name = 'otro precio de compra'
		verbose_name_plural = 'otros precios de compra'

	producto = models.ForeignKey(Producto)
	unidad_medida = models.ForeignKey(UnidadMedida)

	precio_compra = models.DecimalField("Precio de compra", max_digits=15,decimal_places=2)
	factor_conversion = models.DecimalField("Factor de conversion", max_digits=15,decimal_places=2, help_text="Numero a multiplicar para convertir en la unidad de medida principal")

	def __unicode__(self):
		return self.unidad_medida.abreviatura 

	def __str__(self):
		return separador_de_miles(self.precio_compra) + " Gs/" + self.unidad_medida.abreviatura 





class InsercionInmediata(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	observacion = models.CharField(max_length=50, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		verbose_name = 'Insercion Inmediata'
		verbose_name_plural = 'Inserciones Inmediatas'


class SustraccionInmediata(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	observacion = models.CharField(max_length=50, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		verbose_name = 'Sustraccion Inmediata'
		verbose_name_plural = 'Sustracciones Inmediatas'


