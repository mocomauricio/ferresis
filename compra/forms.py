from dal import autocomplete
from django import forms
from compra.models import Compra, DetalleCompra
from producto.models import *

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('__all__')
        widgets = {
            "proveedor": autocomplete.ModelSelect2(url='/admin/proveedor/proveedor/proveedorautocomplete/'),
            "total":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "descuento":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['total'].widget.attrs['readonly'] = True

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
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
        super(DetalleCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['precio'].widget.choices = (('','-------'),) + tuple(PrecioCompraProducto.objects.filter(producto_id = instance.producto.id).values_list('id','unidad_medida__nombre'))
            self.initial['precio'] = instance.precio_id

        self.fields['subtotal'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        detalle = super(DetalleCompraForm, self).save(commit=False)
        detalle.precio_id = self.cleaned_data.get('precio')

        if commit:
            detalle.save()
        return detalle

