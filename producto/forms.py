from dal import autocomplete
from django import forms
from producto.models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')

    precio_venta = forms.IntegerField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}), required=True, label="Precio de venta")
    precio_compra = forms.IntegerField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}), required=True, label="Precio de compra")
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all(), required=True, label='Unidad de medida')

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['precio_venta'] = (PrecioVentaProducto.objects.filter(producto_id=instance.id)[0]).precio_venta
            self.initial['precio_compra'] = (PrecioCompraProducto.objects.filter(producto_id=instance.id)[0]).precio_compra

class InsercionInmediataForm(forms.ModelForm):
    class Meta:
        model = InsercionInmediata
        fields = ('__all__')
        widgets = {
        	"producto": autocomplete.ModelSelect2(url='/admin/producto/producto/productoautocomplete/'),
            "cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
       	}

class SustraccionInmediataForm(forms.ModelForm):
    class Meta:
        model = SustraccionInmediata
        fields = ('__all__')
        widgets = {
        	"producto": autocomplete.ModelSelect2(url='/admin/producto/producto/productoautocomplete/'),
            "cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
        
class PrecioVentaProductoForm(forms.ModelForm):
    class Meta:
        model = PrecioVentaProducto
        fields = ('__all__')
        widgets = {
            "precio_venta":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "factor_conversion":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
       	}
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all(), required=True, label='Unidad de medida')

class PrecioCompraProductoForm(forms.ModelForm):
    class Meta:
        model = PrecioCompraProducto
        fields = ('__all__')
        widgets = {
            "precio_compra":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "factor_conversion":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all(), required=True, label='Unidad de medida')
