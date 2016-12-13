from __future__ import unicode_literals
from django.db import models
from cliente.models import Cliente 
from producto.models import Producto, UnidadMedida, PrecioVentaProducto
from datetime import datetime

# Create your models here.
CONDICION = (('CONTADO', 'CONTADO'),('CREDITO','CREDITO'))

class Presupuesto(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha = models.DateField(default=datetime.now)
	descuento = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	total = models.DecimalField(max_digits=15,decimal_places=2, default=0)

	def __unicode__(self):
		return "Nro. " + str(self.id)

	class Meta:
		verbose_name = 'Presupuesto'
		verbose_name_plural = 'Presupuestos'

class DetallePresupuesto(models.Model):
	presupuesto = models.ForeignKey(Presupuesto)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	precio = models.ForeignKey(PrecioVentaProducto)
	descuento = models.DecimalField(max_digits=15,decimal_places=2, default=0)
	subtotal = models.DecimalField(max_digits=15,decimal_places=2, default=0)

	