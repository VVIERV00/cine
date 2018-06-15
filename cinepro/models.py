# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comentario(models.Model):
    idcomentario = models.AutoField(db_column='idComentario', primary_key=True)  # Field name made lowercase.
    texto = models.CharField(max_length=250)
    pelicula = models.IntegerField()
    def __str__(self):
        return self.texto
    class Meta:
        managed = False
        db_table = 'comentario'


class Pelicula(models.Model):
    idpelicula = models.AutoField(db_column='idPelicula', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=300)
    director = models.CharField(max_length=100)
    def __str__(self):
        return str(self.titulo + ": por " + self.director +".\nSinopsis: " + self.sinopsis + "\nGenero: " + self.genero + '.')
    class Meta:
        managed = False
        db_table = 'pelicula'


class Sala(models.Model):
    idsala = models.IntegerField(db_column='idSala', primary_key=True)  # Field name made lowercase.
    filas = models.IntegerField()
    columnas = models.IntegerField()
    ultimafila = models.IntegerField(db_column='ultimaFila')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sala'


class Sesa(models.Model):
    idsesa = models.AutoField(db_column='idSesa', primary_key=True)  # Field name made lowercase.
    idsesion = models.IntegerField(db_column='idSesion')  # Field name made lowercase.
    idsala = models.IntegerField(db_column='idSala')  # Field name made lowercase.
    ocupacion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sesa'


class Sesion(models.Model):
    idsesion = models.AutoField(db_column='idSesion', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    idpelicula = models.IntegerField(db_column='idPelicula')  # Field name made lowercase.
    idsesa = models.IntegerField(db_column='idSesa')  # Field name made lowercase.

    def __str__(self):
        return self.fecha.strftime('%m/%d/%Y')
    class Meta:
        managed = False
        db_table = 'sesion'
