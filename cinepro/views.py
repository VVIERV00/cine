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
import operator

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

        listSesiones = {}
        idSala = []
        print(sesiones)
        for sesion in sesiones:
            idSala = []
            id = sesion.idsesion
            sesas = Sesa.objects.filter(idsesion=id)
            for sesa in sesas:
                idSala.append(sesa.idsala)

            listSesiones[sesion.idsesion] = {'sala': idSala, 'fecha': sesion.fecha}

        form = ComentarioForm(peticion.POST)
        if form.is_valid():
            comentario = form.save(commit = False)
            comentario.pelicula = idPelicula
            comentario.save()
        else:
            form = ComentarioForm()
        print(listSesiones)

    except:
        raise Http404("No se ha podido encontrar la pelicula %d".format(idPelicula))
    return render(peticion, 'pelicula/index.html', { 'ruta': "../", 'movie':pelicula, 'comentarios':comentarios, 'sesiones':listSesiones, 'id':idPelicula, 'form': form})


"""
    metodo que devuelve un json 'salas' 
    debe ser un array con el id de las salas que se solicitan segun la sesion


"""





"""
    metodo que devuelve un json 'sala' con el 
    numero de filas, columnas y butacas de la ultima fila y tambien devuelve un 
    array de ocupaciones que hay que sacar del objeto sesion. 


"""
@csrf_exempt
def sala(peticion, pelicula, fecha, sala):
    print("ENTRAAAA")
    try:
        peliculaO = Pelicula.objects.filter(idpelicula=pelicula)
        comentarios = Comentario.objects.filter(pelicula=pelicula)
        sesiones = Sesion.objects.filter(idpelicula=pelicula)

        listSesiones = {}
        idSala = []
        print("hola")

        print("hola")
        for sesion in sesiones:
            idSala = []
            id = sesion.idsesion
            sesas = Sesa.objects.filter(idsesion=id)

            for sesa in sesas:
                idSala.append(sesa.idsala)

            listSesiones[sesion.idsesion] = {'sala': idSala, 'fecha': sesion.fecha}

        form = ComentarioForm(peticion.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.pelicula = pelicula
            comentario.save()
        else:
            form = ComentarioForm()

        #segunda parte
        salaO = Sala.objects.filter(idsala=sala)

        sesa = Sesa.objects.filter(idsala = sala, idsesion = fecha)

        list = []

        list.append(range(salaO[0].filas))
        list.append(range(salaO[0].columnas))
        list.append(range(salaO[0].ultimafila))
        list.append(sesa[0].ocupacion)


    except:
        raise Http404("No se ha podido encontrar la sala")
    return render(peticion, 'pelicula/index.html', { 'ruta': "../../../",'listaSalas':list, 'ncol':salaO[0].columnas, 'nfil':salaO[0].filas, 'movie':peliculaO, 'comentarios':comentarios, 'sesiones':listSesiones, 'id':pelicula, 'form': form})


"""
    metodo que rescata los objetos sesion y actualiza los valores necesarios 
    es decir, el array de ocupacion (¡se enviaran y sacaran con POST!) y se hace un .save()
    La idea es llamar a este metodo tantas veces como sesiones haya en la pagina
    peliculas/index.html. habrá sesiones que no se tocan y otras que si, eso se 
    lo dejamos a django.

"""
@csrf_exempt
def reservar(peticion, fecha, pelicula, sala):
    try:
        viejaSesa =  Sesa.objects.filter(idsesion=fecha, idsala=sala)
        lista = peticion.POST.getlist('ocupacion[]')
        texto =''.join(map(str, lista))
        Sesa.objects.filter(idsesion=fecha, idsala=sala).update(ocupacion=texto)
        sesion = Sesion.objects.filter(idpelicula=pelicula)
        sala = Sala.objects.filter(idsala = sala)

        vOcupacion = viejaSesa.ocupacion
        posiciones = []

        i = 0
        while i < len(texto):
            if(vOcupacion[i] != texto[i] ):
                posiciones.append(i)
            i += 1
        filas = []
        columnas = []


        for val in posiciones:
            col = val % sala.columnas
            columnas.insert(col+1)
            valor = sala.filas
            resto = 0
            fila = 0
            while resto < valor:
                resto = valor - val
                fila = fila + 1

            filas.insert(fila+1)

    except:
        return HttpResponse("Ocurrio un error en la reserva")
    return render(peticion,  'pelicula/confirmacion.html', {'sesion':sesion[0], 'columnas':columnas, 'filas':filas })




