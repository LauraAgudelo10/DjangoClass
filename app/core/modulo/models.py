from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser

# Create your models here.
# Modelo de base datos
# Crear la estructura de la aplicación con el módelo de datos

class TipoDocu(models.Model):
    NombTiDoc = models.CharField(max_length = 50, verbose_name = "Nombre Tipo de Documento")

    #Clases Meta=Sirven para indicar como quiero que se llamen mis cosas
    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"

    #Creo la función para llamar atributos:

    def __str__(self):
        return self.NombTiDoc

class CategProye(models.Model):
    lenguaje = models.CharField(max_length = 50, null = True, verbose_name = "Lenguaje del Proyecto")
    motorDB = models.CharField(max_length = 200, null = True, verbose_name = "Base de Datos utilizada para el proyecto")
    arquitectura = models.CharField(max_length = 300, null = True, verbose_name = "Arquitectura del Proyecto")

    class Meta:
        verbose_name = "Categoría del Proyecto"
        verbose_name_plural = "Categorías"

    #Función de Categoria Proyecto

    def __str__(self):
        return self.arquitectura

class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE, verbose_name="Identificador de Categoría")
    fechaInicio = models.DateTimeField(auto_now_add = True, null= True, verbose_name = "Fecha de inicio")
    fechaFin = models.DateTimeField(auto_now = True, null= True, verbose_name = "Fecha de fin")
    nombProyecto = models.CharField(max_length = 100, verbose_name = "Nombre del Proyecto")
    estaProyecto = models.CharField(max_length = 100, verbose_name = "Estado del Proyecto")
    urlRepo =  models.TextField(verbose_name = "Enlace de repositorio")
    descProyecto = models.TextField(verbose_name="Descripción del Proyecto")
    imgProyecto = models.ImageField(upload_to="proyectos", verbose_name = "Icono del Proyecto")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    #Función de mostrar:
    def __unicode__(self):
        return self.nombProyecto


class Documentos(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name = "Identificación de Tipo de Documento")
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE, verbose_name = "Identificación dl proyecto")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificación de usuario")
    nombDocu = models.CharField(max_length = 100, verbose_name = "Nombre de Documento")
    pathDocu = models.CharField(max_length = 100, verbose_name = "Ruta de Almacenamiento")

    class Meta:
        verbose_name = "Documento del Proyecto"
        verbose_name_plural = "Documentos del Proyecto"

    def __unicode__(self):
        return self.nombDocu