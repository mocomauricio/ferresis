from django.contrib import admin
from presupuesto.models import Presupuesto, DetallePresupuesto
from presupuesto.forms import PresupuestoForm, DetallePresupuestoForm

# Register your models here.

class DetallePresupuestoInline(admin.TabularInline):
    model = DetallePresupuesto
    form = DetallePresupuestoForm
    extra = 0

class PresupuestoAdmin(admin.ModelAdmin):
	inlines = (DetallePresupuestoInline,)
	form = PresupuestoForm
	list_display = ('id', 'fecha', 'cliente', 'total')
	ordering = ('-fecha',)
	search_fields = ('id','fecha','cliente__nombre')


admin.site.register(Presupuesto, PresupuestoAdmin)