from django import forms

from . import models
from year import models as m


class ProfesorForm(forms.ModelForm):



    class Meta:
        model = models.profesor
        fields = "__all__"

        widgets = {

            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contacto": forms.EmailInput()
           
        }


   