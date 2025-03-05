from django.db import models
from django.core.exceptions import ValidationError

class Empresa(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proveedor(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.19)  # IVA del 19% por defecto
    precio_venta_sin_iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio sin IVA")
    precio_venta_con_iva = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Precio con IVA")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

    def save(self, *args, **kwargs):
        """Calcula el precio con IVA automáticamente al guardar el producto."""
        self.precio_venta_con_iva = self.precio_venta_sin_iva * (1 + self.iva)
        super().save(*args, **kwargs)

    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto."""
        self.stock_actual += cantidad
        self.save()


class Cotizacion(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=50, default="Pendiente")
    observaciones = models.TextField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cotización {self.numero}"

    @property
    def total(self):
        """Calcula el total de la cotización sumando los subtotales de los detalles."""
        detalles = self.detallecotizacion_set.all()
        return sum(detalle.total for detalle in detalles)


class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_sin_iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario sin IVA")
    precio_unitario_con_iva = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Precio unitario con IVA")
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cotizacion.numero} - {self.producto.nombre}"

    def save(self, *args, **kwargs):
        """Calcula el precio con IVA automáticamente al guardar el detalle."""
        self.precio_unitario_con_iva = self.precio_unitario_sin_iva * (1 + self.producto.iva)
        super().save(*args, **kwargs)

    @property
    def subtotal_sin_iva(self):
        """Calcula el subtotal sin IVA (cantidad * precio_unitario_sin_iva)."""
        return self.cantidad * self.precio_unitario_sin_iva

    @property
    def iva(self):
        """Calcula el IVA (subtotal_sin_iva * porcentaje de IVA del producto)."""
        return self.subtotal_sin_iva * self.producto.iva

    @property
    def subtotal_con_iva(self):
        """Calcula el subtotal con IVA (subtotal_sin_iva + iva)."""
        return self.subtotal_sin_iva + self.iva

    @property
    def total(self):
        """Calcula el total (subtotal_con_iva - descuento)."""
        return self.subtotal_con_iva - self.descuento


class Factura(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default="Pendiente")
    observaciones = models.TextField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.numero}"

    @property
    def total(self):
        """Calcula el total de la factura sumando los subtotales de los detalles."""
        detalles = self.detallefactura_set.all()
        return sum(detalle.total for detalle in detalles)


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_sin_iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario sin IVA")
    precio_unitario_con_iva = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Precio unitario con IVA")
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.factura.numero} - {self.producto.nombre}"

    def save(self, *args, **kwargs):
        """Calcula el precio con IVA automáticamente al guardar el detalle."""
        self.precio_unitario_con_iva = self.precio_unitario_sin_iva * (1 + self.producto.iva)
        super().save(*args, **kwargs)

    @property
    def subtotal_sin_iva(self):
        """Calcula el subtotal sin IVA (cantidad * precio_unitario_sin_iva)."""
        return self.cantidad * self.precio_unitario_sin_iva

    @property
    def iva(self):
        """Calcula el IVA (subtotal_sin_iva * porcentaje de IVA del producto)."""
        return self.subtotal_sin_iva * self.producto.iva

    @property
    def subtotal_con_iva(self):
        """Calcula el subtotal con IVA (subtotal_sin_iva + iva)."""
        return self.subtotal_sin_iva + self.iva

    @property
    def total(self):
        """Calcula el total (subtotal_con_iva - descuento)."""
        return self.subtotal_con_iva - self.descuento

    def save(self, *args, **kwargs):
        """Valida el stock y lo actualiza al guardar el detalle."""
        if self.cantidad > self.producto.stock_actual:
            raise ValidationError(f"No hay suficiente stock para {self.producto.nombre}. Stock disponible: {self.producto.stock_actual}")
        super().save(*args, **kwargs)
        self.producto.actualizar_stock(-self.cantidad)  # Reduce el stock


class Movimiento(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, default="Activo")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.fecha}"


class DetalleMovimiento(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.movimiento.tipo} - {self.producto.nombre}"

    @property
    def total(self):
        """Calcula el total (cantidad * valor_unitario)."""
        return self.cantidad * self.valor_unitario

    def save(self, *args, **kwargs):
        """Actualiza el stock del producto según el tipo de movimiento."""
        super().save(*args, **kwargs)
        if self.movimiento.tipo == 'ENTRADA':
            self.producto.actualizar_stock(self.cantidad)
        elif self.movimiento.tipo == 'SALIDA':
            self.producto.actualizar_stock(-self.cantidad)