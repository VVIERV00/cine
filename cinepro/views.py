from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
def index(peticion):
    try:
        lista = Pelicula.objects.all()
        generos = {"acción", "romantica", "terror", "ciencia-ficcion"}
    except:
        raise Http404('No se ha podido encontrar la cartelera')
    return render(peticion, 'cartelera/index.html', {'listaPeliculas': lista, 'listaGeneros':generos})


def pelicula(peticion, idPelicula):
    try:
        pelicula = Pelicula.objects.filter(idPelicula = idPelicula)
        comentarios = Comentario.objects.filter(pelicula = idPelicula)

    except:
        raise Http404("No se ha podido encontrar la pelicula %d".format(idPelicula))
    return render(peticion, 'pelicula/index.html', {'pelicula':pelicula, 'comentarios':comentarios})

