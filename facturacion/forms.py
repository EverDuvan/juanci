from django import forms
from django.forms import inlineformset_factory
from .models import DetalleCotizacion, DetalleFactura, Producto, Cotizacion, Factura, Movimiento

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

# Crea un formulario en línea para los detalles de la factura
DetalleFacturaFormSet = inlineformset_factory(
    Factura,  # Modelo principal
    DetalleFactura,  # Modelo relacionado
    fields=('producto', 'cantidad', 'precio_unitario_sin_iva', 'descuento'),  # Campos a incluir
    extra=1,  # Número de formularios vacíos para agregar productos
)

# Crea un formulario en línea para los detalles de la cotización
DetalleCotizacionFormSet = inlineformset_factory(
    Cotizacion,  # Modelo principal
    DetalleCotizacion,  # Modelo relacionado
    fields=('producto', 'cantidad', 'precio_unitario_sin_iva', 'descuento'),  # Campos a incluir
    extra=1,  # Número de formularios vacíos para agregar productos
)