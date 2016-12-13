from django.contrib import admin
from cliente.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'ruc', 'telefono',)
	ordering = ('nombre',)
	search_fields = ('nombre','ruc')

admin.site.register(Cliente, ClienteAdmin)