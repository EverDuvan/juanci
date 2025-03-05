from django import forms
from .models import Producto, Cotizacion, Factura, Movimiento

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'