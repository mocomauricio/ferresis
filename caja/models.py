from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AperturaCaja(models.Model):
	usuario = models.ForeignKey(User)
	monto = models.DecimalField(max_digits=15,decimal_places=2)
	fecha_hora = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return (self.usuario.get_full_name() + '-' + self.fecha_hora.strftime('%d/%m/%Y %H:%M:%S'))

	class Meta:
		verbose_name = 'Apertura de Caja'
		verbose_name_plural = 'Aperturas de Caja'


class CierreCaja(models.Model):
	usuario = models.ForeignKey(User)
	monto = models.DecimalField(max_digits=15,decimal_places=2)
	fecha_hora = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return (self.usuario.get_full_name() + '-' + self.fecha_hora.strftime('%d/%m/%Y %H:%M:%S'))

	class Meta:
		verbose_name = 'Cierre de Caja'
		verbose_name_plural = 'Cierres de Caja'