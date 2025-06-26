print("Cargando blog.urls")
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.lista_public, name='lista_public'),
    path('evaluacion2/', views.lista_marcas, name='evaluacion2'),
 HEAD
]

]
 8f1c4d3 (Actualizo proyecto con modelo Marca, vistas y templates)
