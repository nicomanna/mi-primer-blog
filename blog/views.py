from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion, Marca


def lista_public(request):
    publicaciones = Publicacion.objects.filter(
        fecha_publicacion__lte=timezone.now()
    ).order_by('-fecha_publicacion')  # más recientes primero
    return render(request, 'blog/lista_public.html', {'publicaciones': publicaciones})

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'blog/lista_marcas.html', {'marcas': marcas})

    
