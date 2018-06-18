"""cinepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = 'cinepro'

urlpatterns = [
    path('', views.index, name='index'),
    path('cartelera', views.index, name='index'),
    path('pelicula/<int:idPelicula>', views.pelicula, name='pelicula'),
    path('pelicula/<int:pelicula>/<int:fecha>/<int:sala>', views.sala, name='sala'),

    path('pelicula/<int:idPelicula>/confirmacion', views.pelicula, name='confirmacion'),

    path('sesion/<int:fecha>/<int:pelicula>/<int:sala>/reservar', views.reservar, name='reservar')

]

