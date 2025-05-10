Juanci es una aplicación web diseñada para manejo de clientes, proveedores, productos etc de una distribuidora.

📌 Tabla de Contenidos
Características

Tecnologías

Instalación

Estructura del Proyecto

Uso

Desarrollo

Contribución

Licencia

Contacto

✨ Características Principles
✅ Diseño Responsive - Adaptable a móviles, tablets y desktop.
✅ Interfaz Intuitiva - Fácil navegación y experiencia de usuario optimizada.
✅ Rendimiento Optimizado - Carga rápida gracias a buenas prácticas de desarrollo.
✅ [Otra característica destacable] - [Breve descripción].

🛠 Tecnologías Utilizadas
Frontend
HTML5 - Estructura semántica.

CSS3 - Estilos personalizados y animaciones.

JavaScript (ES6+) - Interactividad dinámica.

Bootstrap 5 - Framework CSS para diseño responsivo.

Herramientas
Git - Control de versiones.

GitHub - Alojamiento del repositorio.

⚙️ Instalación y Configuración
Requisitos Previos
Navegador moderno (Chrome, Firefox, Edge).

Pasos para Instalación
Clonar el repositorio (o descargar como ZIP):

sh
git clone https://github.com/EverDuvan/juanci.git
cd juanci
Abrir en el navegador:

Simplemente abre index.html en tu navegador favorito.

📂 Estructura del Proyecto
juanci/
├── css/                  # Estilos personalizados (CSS)
│   └── styles.css        
├── img/                  # Imágenes y recursos visuales
├── js/                   # Lógica de JavaScript
│   └── script.js         
├── index.html            # Página principal
└── README.md             # Este archivo
🚀 ¿Cómo Usar?
Navegación básica:

Usa el menú superior para acceder a diferentes secciones.

Personalización:

🔧 Desarrollo
Modo de Desarrollo
Si deseas modificar el código:

Edita los archivos HTML/CSS/JS según necesites.

Usa Live Server (extensión de VSCode) para previsualizar cambios en tiempo real.

Pruebas
Abre la aplicación en diferentes navegadores para verificar compatibilidad.

🤝 Contribución
¡Las contribuciones son bienvenidas! Sigue estos pasos:

Haz un Fork del proyecto.

Crea una Rama (git checkout -b feature/nueva-funcionalidad).

Haz Commit de tus cambios (git commit -m 'Añade nueva funcionalidad').

Haz Push a la rama (git push origin feature/nueva-funcionalidad).

Abre un Pull Request y describe tus cambios.

📜 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

📩 Contacto
Ever Duvan

📧 everduvanhdez@gmail.com

🌐 GitHub

🔗 Enlace del Proyecto: https://github.com/EverDuvan/juanci

✨ ¡Gracias por tu interés en Juanci!
Si tienes preguntas o sugerencias, no dudes en contactarme. 🚀



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
