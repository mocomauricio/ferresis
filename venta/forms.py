from dal import autocomplete
from django import forms
from venta.models import *
from producto.models import *

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('__all__')
        widgets = {
            "cliente": autocomplete.ModelSelect2(url='/admin/cliente/cliente/clienteautocomplete/'),
            "total":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "descuento":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['total'].widget.attrs['readonly'] = True

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        #fields = ('__all__')
        exclude = ['precio',]
        widgets = {
            "producto": autocomplete.ModelSelect2(url='/admin/producto/producto/productoautocomplete/'),
            "cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "subtotal":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }

    precio = forms.IntegerField(widget=forms.Select(choices=(('','-------'),)), label="unidad de medida")

    def __init__(self, *args, **kwargs):
        super(DetalleVentaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['precio'].widget.choices = (('','-------'),) + tuple(PrecioVentaProducto.objects.filter(producto_id = instance.producto.id).values_list('id','unidad_medida__nombre'))
            self.initial['precio'] = instance.precio_id

        self.fields['subtotal'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        detalle = super(DetalleVentaForm, self).save(commit=False)
        detalle.precio_id = self.cleaned_data.get('precio')

        if commit:
            detalle.save()
        return detalle