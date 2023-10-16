from django import forms

from . import models
from year import models as m


class AlumnoForm(forms.ModelForm):


    anio = forms.ModelChoiceField(queryset= m.year.objects.all() )


    class Meta:
        model = models.alumno
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "escuela": forms.TextInput(attrs={"class": "form-control"}),
           
        }


   