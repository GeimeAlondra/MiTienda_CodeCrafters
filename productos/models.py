from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50,verbose_name="Nombre Producto")
    descripcion = models.TextField(null=False, max_length=200,verbose_name="Descrpcion Producto")
    fechaProduccion = models.TextField(null=False,verbose_name="FechaProducion Producto")
    fechaVencimiento = models.DateField(null=False,verbose_name="FechaVencimiento Producto")
    existencias = models.IntegerField(null=False,verbose_name="Existencias Producto")
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=9,verbose_name="Precio Producto")
    categoria = models.TextField(null=False, max_length=50,verbose_name="Categoria Producto")
    proveedor = models.TextField(null=False, max_length=100,verbose_name="Proveedor Producto")
    imagen = models.ImageField(null=True,upload_to='img/productos')
    
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50,verbose_name="Nombre")
    email = models.EmailField(null=False, max_length=50,verbose_name="Correo Electronico")
    Mensaje = models.TextField(null=False, max_length=50,verbose_name="Mensaje")