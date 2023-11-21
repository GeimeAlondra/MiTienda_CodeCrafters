from django.db import models
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=60,verbose_name="Nombre de Producto")
    descripcion = models.TextField(null=False, max_length=200,verbose_name="Descripción")
    fechaProduccion = models.TextField(null=False,verbose_name="Fecha de Producción")
    fechaVencimiento = models.DateField(null=False,verbose_name="Fecha de Vencimiento")
    existencias = models.IntegerField(null=False,verbose_name="Existencias")
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=9,verbose_name="Precio de Venta")
    categoria = models.TextField(null=False, max_length=75,verbose_name="Categoría")
    proveedor = models.TextField(null=False, max_length=150,verbose_name="Proveedor")
    imagen = models.ImageField(null=True,upload_to='img/productos')
   
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50,verbose_name="Nombre")
    email = models.EmailField(null=False, max_length=100,verbose_name="Correo Electrónico")
    Mensaje = models.TextField(null=False, max_length=200,verbose_name="Mensaje")

