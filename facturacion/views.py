from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cotizacion, Factura, Movimiento
from .forms import DetalleCotizacionFormSet, DetalleFacturaFormSet, ProductoForm, CotizacionForm, FacturaForm, MovimientoForm

def inicio(request):
    return render(request, 'facturacion/inicio.html')

# Vistas para Producto
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'facturacion/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'facturacion/crear_producto.html', {'form': form})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'facturacion/detalle_producto.html', {'producto': producto})

# Vistas para Cotización
def lista_cotizaciones(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'facturacion/lista_cotizaciones.html', {'cotizaciones': cotizaciones})

def crear_cotizacion(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        formset = DetalleCotizacionFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            cotizacion = form.save()  # Guarda la cotización
            formset.instance = cotizacion  # Asocia los detalles con la cotización
            formset.save()  # Guarda los detalles
            return redirect('lista_cotizaciones')  # Redirige a la lista de cotizaciones
    else:
        form = CotizacionForm()
        formset = DetalleCotizacionFormSet()
    return render(request, 'facturacion/crear_cotizacion.html', {'form': form, 'formset': formset})

# Vistas para Factura
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturacion/lista_facturas.html', {'facturas': facturas})

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturacion/detalle_factura.html', {'factura': factura})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        formset = DetalleFacturaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            factura = form.save()  # Guarda la factura
            formset.instance = factura  # Asocia los detalles con la factura
            formset.save()  # Guarda los detalles
            return redirect('lista_facturas')  # Redirige a la lista de facturas
    else:
        form = FacturaForm()
        formset = DetalleFacturaFormSet()
    return render(request, 'facturacion/crear_factura.html', {'form': form, 'formset': formset})

# Vistas para Movimiento
def lista_movimientos(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'facturacion/lista_movimientos.html', {'movimientos': movimientos})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_movimientos')
    else:
        form = MovimientoForm()
    return render(request, 'facturacion/crear_movimiento.html', {'form': form})