
from django.contrib import admin
from . import models



@admin.register(models.clase_particular)
class clase_particularAdmin(admin.ModelAdmin):
   


    list_display = ("fecha", "hora_inicio", "hora_fin","alumno", "profesor_materia", "comentarios")
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    ordering = ("fecha",)