from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('cotizaciones/<int:pk>/', views.detalle_factura, name='detalle_cotizacion'),
    path('cotizaciones/', views.lista_cotizaciones, name='lista_cotizaciones'),
    path('cotizaciones/crear/', views.crear_cotizacion, name='crear_cotizacion'),
    path('facturas/<int:pk>/', views.detalle_factura, name='detalle_factura'),
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('facturas/crear/', views.crear_factura, name='crear_factura'),
    path('movimientos/', views.lista_movimientos, name='lista_movimientos'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('obtener-stock/<int:producto_id>/', views.obtener_stock, name='obtener_stock'),
]