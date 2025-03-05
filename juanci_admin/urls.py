from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('facturacion/', include('facturacion.urls')),  # URLs de la aplicación de facturacion
    path('', include('facturacion.urls')),  # Redirige la URL raíz a la aplicación de facturacion
]

# Sirve archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)