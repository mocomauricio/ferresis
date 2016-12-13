from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
CONDICION = (('CONTADO', 'CONTADO'),('CREDITO','CREDITO'))

class Compra(models.Model):
	numero_factura = models.CharField(max_length=20, null=True, blank=True)
	proveedor = models.ForeignKey('proveedor.Proveedor', null=True, blank=True)
	condicion = models.CharField(choices=CONDICION, max_length = 10, default='CONTADO')
	fecha = models.DateField(default=datetime.now)
	descuento = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	total = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	carga_inicial = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.numero_factura

	class Meta:
		verbose_name = 'Compra'
		verbose_name_plural = 'Compras'

class DetalleCompra(models.Model):
	compra = models.ForeignKey(Compra)
	producto = models.ForeignKey('producto.Producto')
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.ForeignKey('producto.PrecioCompraProducto', verbose_name="unidad de medida")
	precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)


