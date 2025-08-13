from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('<int:categoria_id>/', views.filtrar_por_categoria, name='filtrar_categoria'),
]