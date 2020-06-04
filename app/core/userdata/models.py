from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos
# Create your models here.
# Modelo de base datos
# Crear la estructura de la aplicación con el módelo de datos

class Roles(models.Model):
    RoleName = models.CharField(max_length = 50, verbose_name = "Roles")

    #Clases Meta=Sirven para indicar como quiero que se llamen mis cosas
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"


    #Creo la función para llamar atributos:

    def __str__(self):
        return self.RoleName

class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20, verbose_name = "Identificación")
    nombUser = models.CharField(max_length = 100, null= True, verbose_name = "Nombres")
    apelUser = models.CharField(max_length = 100, null= True, verbose_name = "Apellidos")
    profeUser = models.CharField(max_length = 100, null= True, verbose_name = "Profesión")
    fotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="img/perfiles")
    teleUser = models.CharField(max_length = 20, verbose_name = "Número de Teléfono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = "Otro", verbose_name = "Género")
    adddata = models.DateTimeField(auto_now_add = True, null= True, verbose_name = "Creado el")
    modifiat = models.DateTimeField(auto_now = True, null= True, verbose_name = "Modificado el")

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"

    #Función de DatosUser
    def __str__(self):
        return self.nombUser

class HabilUser(models.Model):
    NombHabil = models.CharField(max_length = 100, verbose_name = "Nombre de la habilidad")
    DescHabil = models.TextField(verbose_name="Descripción de la habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

    #Función de Habilidades
    def __str__(self):
        return self.NombHabil

class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name="Identificador de rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificación de usuario")
    addUser = models.DateTimeField(auto_now_add = True, null= True, verbose_name = "Fecha de agregación")
    udtuser = models.DateTimeField(auto_now = True, null= True)
    estaRol = models.CharField(max_length = 10, verbose_name = "Estado de Rol")

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"
    #Función de mostrar:
    def __unicode__(self):
        return self.idRole

class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE, verbose_name = "Identificación de habilidad")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificación de usuario")
    pcrHabil = models.DecimalField(max_digits = 2, decimal_places = 1 , verbose_name = "Porcentaje de habilidad")
    udtHabil = models.DateTimeField(auto_now = True, null= True)

    class Meta:
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuario"

    def __unicode__(self):
        return self.idUser