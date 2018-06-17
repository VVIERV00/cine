from builtins import list

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from .form import ComentarioForm
import datetime
from django.core import serializers
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(peticion):
    try:
        peliculasValidas = Sesion.objects.values('idpelicula').filter(fecha__gte=datetime.date.today())

        lista = Pelicula.objects.filter(idpelicula__in=peliculasValidas)
        generos = {"acción", "romantica", "terror", "ciencia-ficcion"}
    except:
        raise Http404('No se ha podido encontrar la cartelera')
    return render(peticion, 'cartelera/index.html', {'listaPeliculas': lista, 'listaGeneros':generos})

@csrf_exempt
def pelicula(peticion, idPelicula):
    try:
        pelicula = Pelicula.objects.filter(idpelicula = idPelicula)
        comentarios = Comentario.objects.filter(pelicula = idPelicula)
        sesiones = Sesion.objects.filter(idpelicula = idPelicula)

        for sesion in sesiones:
            id = sesion.idsesion

        sesas = Sesa.objects.filter(idsesion = id)

        for sesa in sesas:
            idSala = sesa.idsala

        salas = Sala.objects.filter(idsala =  idSala)

        form = ComentarioForm(peticion.POST)
        if form.is_valid():
            post = form.save()
            post.save()
        else:
            form = ComentarioForm()
            form.fields['pelicula'].initial = idPelicula


    except:
        raise Http404("No se ha podido encontrar la pelicula %d".format(idPelicula))
    return render(peticion, 'pelicula/index.html', {'movie':pelicula, 'comentarios':comentarios, 'sesiones':sesiones, 'id':idPelicula, 'form': form, 'listaSalas':salas, 'filas':range(salas[0].filas), 'columnas':range(salas[0].columnas), 'ultFila':range(salas[0].ultimafila)})


"""
    metodo que devuelve un json 'salas' 
    debe ser un array con el id de las salas que se solicitan segun la sesion


"""
@csrf_exempt
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

    return HttpResponse(json.dumps(data), content_type='application/json')




"""
    metodo que devuelve un json 'sala' con el 
    numero de filas, columnas y butacas de la ultima fila y tambien devuelve un 
    array de ocupaciones que hay que sacar del objeto sesion. 


"""
@csrf_exempt
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

    return HttpResponse(json.dumps(data), content_type='application/json')


"""
    metodo que rescata los objetos sesion y actualiza los valores necesarios 
    es decir, el array de ocupacion (¡se enviaran y sacaran con POST!) y se hace un .save()
    La idea es llamar a este metodo tantas veces como sesiones haya en la pagina
    peliculas/index.html. habrá sesiones que no se tocan y otras que si, eso se 
    lo dejamos a django.

"""
@csrf_exempt
def reservar(peticion, fecha, pelicula, sala):
    pass