from django.db import models
from datetime import datetime


# Create your models here.

class Publicacion (models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    fecha_publicacion = models.DateTimeField(verbose_name='Fecha de Publicación', auto_now=True, auto_now_add=False)
    fotos = models.ImageField(upload_to='fotos', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return self.titulo
        
    class Meta:
        db_table = 'Publicacion'

class Crear_Usuario (models.Model):
    nombre = models.CharField(help_text='Ingrese su nombre', max_length=150)
    apellido = models.CharField(help_text='Ingrese su apellido', max_length=150)
    email = models.EmailField(help_text='Ingrese su E-mail', verbose_name='E-mail', max_length=254)
    contraseña = models.CharField(help_text='Ingrese su contraseña', verbose_name='Contraseña', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'nuevo usuario'
    
