
from django.urls import path
from . import views



app_name = "apps.articulos"

urlpatterns = [
    
    path('Listar', views.Listar_Articulos, name = 'path_listar_articulos'),
    
    
    #path('Detalle/<int:pk>', views.Detalle_Producto, name = "path_detalle_producto"),
    path('Detalle/<int:pk>', views.Detalle_Articulo.as_view(), name = "path_detalle_articulo"),   #Esta vista y la anterior hacen lo mismo. Solo puedo usar una
    
    
    path('Crear/', views.Crear_Articulo.as_view(), name = 'path_crear_articulo'),   #Esto es una opcion para crear articulos
    
    path('Editar/<int:pk>', views.EditarArticuloView.as_view(), name='path_editar_articulo'),
    
    path('Eliminar/<int:pk>', views.EliminarArticuloView.as_view(), name='path_eliminar_articulo'),
    

]

