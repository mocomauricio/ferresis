from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(max_length=100)
	ruc = models.CharField(max_length=20, blank=True)
	direccion = models.CharField(max_length=200, blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	celular = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=100, blank=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'
