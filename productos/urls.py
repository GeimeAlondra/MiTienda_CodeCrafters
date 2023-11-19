from django.urls import path
from productos import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.listado_productos,name="productos"),
    path('productos/crear', views.crearProducto,name="crear_producto"),
    path('productos/editar/<int:id>', views.editarProducto,name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name="eliminar_producto"),
    
    #Contacto
    path('contactos/', views.listado_contactos,name="contactos"),
    path('Contactanos', views.crearContacto,name="contacto"),
    path('contactos/editar/<int:id>', views.editarContacto, name="editar_contacto"),
    path('contactos/eliminar/<int:id>', views.eliminar_contacto, name="eliminar_contacto"),
    
    #Acerca de
    path('acercaDe/', views.acerca_de, name="acercaDe"),
]