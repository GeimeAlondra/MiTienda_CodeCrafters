from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib import messages
from .models import Producto
from .forms import ProductosForm
from. forms import ContactoForm
from datetime import datetime

#existen 2 tipos de parametros que se usan en las peticiones http
# 1- Request (lo que se envia)
# 2- Response (lo que se devuelve)
# Create your views here.
def hola_mundo(request):
    return HttpResponse('<h1>Hola mundo desde Django</h1>')

def inicio(request):
    productos = Producto.objects.all() 
    return render(request, 'pages/inicio.html',{'productos': productos})


#Para Productos
def listado_productos(request):
    productos = Producto.objects.all()    
    return render (request,'producto/producto.html',{'productos': productos})

def crearProducto(request):
    
    formulario = ProductosForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        #producto = formulario.save
        formulario.save()
        messages.success(request,"Creado Satisfactoriamente")
        return redirect('productos')
        
    return render(request,'producto/crear.html', {'formulario': formulario})

def editarProducto(request ,id):
    producto = Producto.objects.get(id = id)

    formulario = ProductosForm(request.POST or None, request.FILES ,instance= producto)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Modificado Satisfactoriamente")
        return redirect('productos')
    
    else:
       # Realiza la conversión de formato de fecha antes de pasarla al formulario.
        # fecha_en_formato_correcto1 = producto.fechaProduccion.strftime('%Y-%m-%d')
        
        fecha_en_formato_correcto2 = producto.fechaVencimiento.strftime('%Y-%m-%d')
        data = { 'fechaVencimiento': fecha_en_formato_correcto2}  
        formulario = ProductosForm(instance=producto, initial=data)
        
    return render(request,'producto/editar.html',{'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    messages.success(request,"Eliminado Satisfactoriamente")
    return redirect('productos')

#Para Contacto
def inicio_contacto(request):
    return render(request,'pages/contacto.html')

def crearContacto(request):    
    formulario = ContactoForm(request.POST or None)
    if formulario.is_valid():
        #producto = formulario.save
        formulario.save()
        return redirect('contacto')
    return render(request,'pages/contacto.html', {'formulario': formulario})
