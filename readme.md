



Rutas

Clientes: http://127.0.0.1:8000/clientes/

Proveedores: http://127.0.0.1:8000/proveedores/

Empleados: http://127.0.0.1:8000/empleados/

Productos: http://127.0.0.1:8000/productos/

Movimientos: http://127.0.0.1:8000/movimientos/

Estructura

gestion_comercial/
│
├── gestion/
│   ├── migrations/
│   ├── templates/
│   │   ├── gestion/
│   │   │   ├── lista_clientes.html
│   │   │   ├── detalle_cliente.html
│   │   │   ├── buscar_cliente.html
│   │   │   ├── agregar_cliente.html
│   │   │   ├── editar_cliente.html
│   │   │   ├── eliminar_cliente.html
│   │   │   ├── (proveedores, empleados, productos y movimientos)
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── gestion_comercial/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── manage.py