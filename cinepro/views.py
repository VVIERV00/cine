from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from .form import ComentarioForm
import datetime
from django.core import serializers


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


"""
    metodo que devuelve un json 'salas' 
    debe ser un array con el id de las salas que se solicitan segun la sesion


"""

def sesion(peticion, fecha, pelicula):
    try:
        sesion = Sesion.objects.filter(fecha = fecha, idpelicula=pelicula)

        list = []

        for ses in sesion:
            list.insert(ses.idsesion)

        data = serializers.serialize('json', list)
        print(data)
    except:
        raise Http404('No se ha podido encontrar la sesion')

    return render(peticion, 'pelicula/index.html',{'salas':data})




"""
    metodo que devuelve un json 'sala' con el 
    numero de filas, columnas y butacas de la ultima fila y tambien devuelve un 
    array de ocupaciones que hay que sacar del objeto sesion. 


"""
def sala(peticion, fecha, pelicula, sala):

    try:
        sala = Sala.objects.filter(idsala=sala)
        sesion = Sesion.objects.filter(fecha=fecha, idpelicula=pelicula)

        for ses in sesion:
            id = ses.idsesion

        sesa = Sesa.objects.filter(idsala = sala, idsesion = id)

        list = []

        for sa in sala:
            list.insert(sa.filas)
            list.insert(sa.columnas)
            list.insert(sa.ultimafila)

        for s in sesa:
            list.insert(s.ocupacion)

        data = serializers.serialize('json', list)
        print(data)
    except:
        raise Http404('No se ha podido encontrar la sala')

    return render(peticion, 'pelicula/index.html', {'sala': data})


"""
    metodo que rescata los objetos sesion y actualiza los valores necesarios 
    es decir, el array de ocupacion (¡se enviaran y sacaran con POST!) y se hace un .save()
    La idea es llamar a este metodo tantas veces como sesiones haya en la pagina
    peliculas/index.html. habrá sesiones que no se tocan y otras que si, eso se 
    lo dejamos a django.

"""

def reservar(peticion, fecha, pelicula, sala):
    pass