from django.contrib import admin
from proveedor.models import Proveedor

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'ruc', 'telefono',)
	ordering = ('nombre',)
	search_fields = ('nombre','ruc')

admin.site.register(Proveedor, ProveedorAdmin)