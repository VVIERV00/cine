from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
import datetime


def index(peticion):
    try:
        peliculasValidas = Sesion.objects.values('idpelicula').filter(fecha__gte=datetime.date.today())

        lista = Pelicula.objects.filter(idpelicula__in=peliculasValidas)
        generos = {"acción", "romantica", "terror", "ciencia-ficcion"}
    except:
        raise Http404('No se ha podido encontrar la cartelera')
    return render(peticion, 'cartelera/index.html', {'listaPeliculas': lista, 'listaGeneros':generos})


def pelicula(peticion, idPelicula):
    try:
        pelicula = Pelicula.objects.filter(idpelicula = idPelicula)
        comentarios = Comentario.objects.filter(pelicula = idPelicula)
        sesiones = Sesion.objects.filter(idpelicula = idPelicula)

    except:
        raise Http404("No se ha podido encontrar la pelicula %d".format(idPelicula))
    return render(peticion, 'pelicula/index.html', {'movie':pelicula, 'comentarios':comentarios, 'sesiones':sesiones})

def enviarComentario(peticion):
    if peticion.method == 'POST':
        comentario = peticion.POST.get('comentario')
        peli = peticion.POST.get('idPelicula')
        objeto = Comentario(texto = comentario, pelicula = peli)
        objeto.save()
        respuesta = {}

    else:
        raise Http404("No se ha podido enviar el comentario, por lo que sea")

