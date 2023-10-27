from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50)
    descripcion = models.TextField(null=False, max_length=200)
    fechaProduccion = models.DateField(null=False)
    fechaVencimiento = models.DateField(null=False)
    existencias = models.IntegerField(null=False)
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=9)
    categoria = models.TextField(null=False, max_length=50)
    proveedor = models.TextField(null=False, max_length=100)