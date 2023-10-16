from django.contrib import admin
from . import models



@admin.register(models.alumno)
class alumnoAdmin(admin.ModelAdmin):
   


    list_display = ("nombre", "escuela", "anio")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)