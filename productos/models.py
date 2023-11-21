from django.db import models
class Producto(models.Model):
   
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50,verbose_name="Nombre")
    email = models.EmailField(null=False, max_length=100,verbose_name="Correo Electrónico")
    Mensaje = models.TextField(null=False, max_length=200,verbose_name="Mensaje")

