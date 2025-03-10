from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Empleado, Producto, Cotizacion, Factura, Movimiento, Proveedor
from .forms import ClienteForm, DetalleCotizacionFormSet, DetalleFacturaFormSet, EmpleadoForm, ProductoForm, CotizacionForm, FacturaForm, MovimientoForm, ProveedorForm

def inicio(request):
    return render(request, 'facturacion/inicio.html')

def obtener_stock(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({'stock_actual': producto.stock_actual})

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

def detalle_cotizacion(request, pk):
    cotizacion = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturacion/detalle_cotizacion.html', {'cotizacion': cotizacion})

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
            factura = form.save()
            formset.instance = factura
            formset.save()
            return redirect('lista_facturas')
    else:
        form = FacturaForm()
        # Inicializar el formset con un formulario vacío
        formset = DetalleFacturaFormSet(initial=[{'cantidad': 0}])
    
    return render(request, 'facturacion/crear_factura.html', {
        'form': form,
        'formset': formset
    })

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

def detalle_movimiento(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    return render(request, 'facturacion/detalle_movimiento.html', {'movimiento': movimiento})

# Vistas para proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('-id')
    return render(request, 'facturacion/lista_proveedores.html', {
        'proveedores': proveedores,
        'titulo': 'Lista de Proveedores'
    })

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    
    return render(request, 'facturacion/crear_proveedor.html', {
        'form': form,
        'titulo': 'Nuevo Proveedor'
    })

def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'facturacion/detalle_proveedor.html', {
        'proveedor': proveedor,
        'titulo': f'Detalle de {proveedor.nombre}'
    })

# Vistas para clientes
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'facturacion/lista_clientes.html', {
        'clientes': clientes,
        'titulo': 'Lista de Clientes'
    })

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'facturacion/crear_cliente.html', {
        'form': form,
        'titulo': 'Nuevo Cliente'
    })

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'facturacion/detalle_cliente.html', {
        'cliente': cliente,
        'titulo': f'Detalle de {cliente.nombre}'
    })







# Vistas para empleados
def lista_empleados(request):
    empleados = Empleado.objects.all().order_by('-id')
    return render(request, 'facturacion/lista_empleados.html', {
        'empleado': empleados,
        'titulo': 'Lista de Empleado'
    })

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    
    return render(request, 'facturacion/crear_empleado.html', {
        'form': form,
        'titulo': 'Nuevo Empleado'
    })

def detalle_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'facturacion/detalle_empleado.html', {
        'empleado': empleado,
        'titulo': f'Detalle de {empleado.nombre}'
    })

def obtener_menu(request):
    return {
        "menu_sections": {
            "Productos": {
                "ver": [{"url": "lista_productos", "icon": "fa-box", "text": "Ver productos"}],
                "crear": [{"url": "crear_producto", "icon": "fa-plus", "text": "Crear producto"}]
            },
            "Proveedores": {
                "ver": [{"url": "lista_proveedores", "icon": "fa-truck", "text": "Ver proveedores"}],
                "crear": [{"url": "crear_proveedor", "icon": "fa-plus", "text": "Crear proveedor"}]
            },
            "Clientes": {
                "ver": [{"url": "lista_clientes", "icon": "fa-users", "text": "Ver clientes"}],
                "crear": [{"url": "crear_cliente", "icon": "fa-plus", "text": "Crear cliente"}]
            },
            "Empleados": {
                "ver": [{"url": "lista_empleados", "icon": "fa-user-tie", "text": "Ver empleados"}],
                "crear": [{"url": "crear_empleado", "icon": "fa-plus", "text": "Crear empleado"}]
            },
            "Cotizaciones": {
                "ver": [{"url": "lista_cotizaciones", "icon": "fa-file-invoice", "text": "Ver cotizaciones"}],
                "crear": [{"url": "crear_cotizacion", "icon": "fa-plus", "text": "Crear cotización"}]
            },
            "Facturas": {
                "ver": [{"url": "lista_facturas", "icon": "fa-file-alt", "text": "Ver facturas"}],
                "crear": [{"url": "crear_factura", "icon": "fa-plus", "text": "Crear factura"}]
            },
            "Movimientos": {
                "ver": [{"url": "lista_movimientos", "icon": "fa-exchange-alt", "text": "Ver movimientos"}],
                "crear": [{"url": "crear_movimiento", "icon": "fa-plus", "text": "Crear movimiento"}]
            }
        }
    }
