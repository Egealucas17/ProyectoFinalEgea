from django.contrib import admin
from django.contrib import admin
from . import models



@admin.register(models.profesor)
class profesorAdmin(admin.ModelAdmin):
   


    list_display = ("nombre", "titulo", "contacto")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)