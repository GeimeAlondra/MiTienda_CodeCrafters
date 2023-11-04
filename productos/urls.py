from django.urls import path
from productos import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.listado_productos,name="productos"),
    path('productos/crear', views.crearProducto,name="crear_producto"),
    path('productos/editar/<int:id>', views.editarProducto,name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name="eliminar_producto"),
    
    #Contacto
    path('Contactanos', views.crearContacto,name="contacto"),
    
]