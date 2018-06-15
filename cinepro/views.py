from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from .form import ComentarioForm
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

        form = ComentarioForm(peticion.POST)
        if form.is_valid():
            post = form.save()
            post.save()
        else:
            form = ComentarioForm()
            form.fields['pelicula'].initial = idPelicula


    except:
        raise Http404("No se ha podido encontrar la pelicula %d".format(idPelicula))
    return render(peticion, 'pelicula/index.html', {'movie':pelicula, 'comentarios':comentarios, 'sesiones':sesiones, 'idPelicula':idPelicula, 'form': form})






