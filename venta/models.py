from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
CONDICION = (('CONTADO', 'CONTADO'),('CREDITO','CREDITO'))

class Venta(models.Model):
	numero_factura = models.CharField(max_length=20, null=True, blank=True)
	cliente = models.ForeignKey('cliente.Cliente', null=True, blank=True)
	condicion = models.CharField(choices=CONDICION, max_length = 10, default='CONTADO')
	fecha = models.DateField(default=datetime.now)
	descuento = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

	def __unicode__(self):
		return self.numero_factura

	class Meta:
		verbose_name = 'Venta'
		verbose_name_plural = 'Ventas'

class DetalleVenta(models.Model):
	venta = models.ForeignKey(Venta)
	producto = models.ForeignKey('producto.Producto')
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.ForeignKey('producto.PrecioVentaProducto', verbose_name="unidad de medida")
	precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)


