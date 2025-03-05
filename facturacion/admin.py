from django.contrib import admin
from .models import Empresa, Cliente, Proveedor, Empleado, Producto, Cotizacion, DetalleCotizacion, Factura, DetalleFactura, Movimiento, DetalleMovimiento

admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Movimiento)
admin.site.register(DetalleMovimiento)