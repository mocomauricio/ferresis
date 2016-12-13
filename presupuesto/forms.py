from dal import autocomplete
from django import forms
from presupuesto.models import Presupuesto, DetallePresupuesto


class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ('__all__')
        widgets = {"cliente": autocomplete.ModelSelect2(url='/admin/cliente/cliente/clienteautocomplete/'),}        
    total = forms.DecimalField(widget=forms.TextInput(attrs={'readonly':'readonly'}),label="Total",required=True)

class DetallePresupuestoForm(forms.ModelForm):
    class Meta:
        model = DetallePresupuesto
        fields = ('__all__')
        widgets = {"producto": autocomplete.ModelSelect2(url='/admin/producto/producto/productoautocomplete/'),}
    subtotal = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'subtotal_iterable', 'readonly':'readonly', 'value':'0'}), label="SUBTOTAL", required=True)   
 
