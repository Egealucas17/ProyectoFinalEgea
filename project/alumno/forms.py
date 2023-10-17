from django import forms

from . import models
from year import models as m


class AlumnoForm(forms.ModelForm):


    class Meta:
        model = models.alumno
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "escuela": forms.TextInput(attrs={"class": "form-control"}),
            "anio": forms.Select(attrs={"class": "form-control"})
           
        }


   