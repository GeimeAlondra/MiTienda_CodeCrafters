from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto
from .forms import ProductosForm
from datetime import datetime

#existen 2 tipos de parametros que se usan en las peticiones http
# 1- Request (lo que se envia)
# 2- Response (lo que se devuelve)
# Create your views here.
def hola_mundo(request):
    return HttpResponse('<h1>Hola mundo desde Django</h1>')

def inicio(request):
    return render(request, 'pages/inicio.html')

def listado_productos(request):
    productos = Producto.objects.all()    
    return render (request,'producto/producto.html',{'productos': productos})

def crearProducto(request):
    
    formulario = ProductosForm(request.POST or None)
    if formulario.is_valid():
        #producto = formulario.save
        formulario.save()
        return redirect('productos')
         
    return render(request,'producto/crear.html', {'formulario': formulario})

def editarProducto(request ,id):
    producto = Producto.objects.get(id = id)

    formulario = ProductosForm(request.POST or None,instance= producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    
    else:
       # Realiza la conversión de formato de fecha antes de pasarla al formulario.
        fecha_en_formato_correcto1 = producto.fechaProduccion.strftime('%Y-%m-%d')
        fecha_en_formato_correcto2 = producto.fechaVencimiento.strftime('%Y-%m-%d')
        data = {'fechaProduccion': fecha_en_formato_correcto1, 'fechaVencimiento': fecha_en_formato_correcto2}  
        formulario = ProductosForm(instance=producto, initial=data)
        
    return render(request,'producto/editar.html',{'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')