from dal import autocomplete
from django import forms
from caja.models import *


class AperturaCajaForm(forms.ModelForm):
    class Meta:
        model = AperturaCaja
        fields = ('__all__' )
        widgets = { 
            "monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }

class CierreCajaForm(forms.ModelForm):
    class Meta:
        model = CierreCaja
        fields = ('__all__' )
        widgets = { 
            "monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }