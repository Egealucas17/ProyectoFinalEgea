from django import forms

from . import models


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = models.alumno
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "escuela": forms.TextInput(attrs={"class": "form-control"}),
            "anio": forms.TextInput(attrs={"class": "form-control"}),
        }


   