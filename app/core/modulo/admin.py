from django.contrib import admin
#Importamos las clases desde los modelos:
from .models import TipoDocu, CategProye, Proyectos, Documentos

# Register your models here.
#Registro del modelo de TipoDocu
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombTiDoc"]

    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)

#Registro del modelo de CategProye
class CategProyeRole(admin.ModelAdmin):
    list_display = ["arquitectura"]

    class Meta:
        model = CategProye
admin.site.register(CategProye)

#Registro del modelo de Proyectos
class ProyectosRole(admin.ModelAdmin):
    list_display = ["nombProyecto"]

    class Meta:
        model = Proyectos
admin.site.register(Proyectos)

#Registro del modelo de Documentos
class DocumentosRole(admin.ModelAdmin):
    list_display = ["nombDocu"]

    class Meta:
        model = Documentos
admin.site.register(Documentos)
