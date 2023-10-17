from django import forms

from . import models


class profesor_materiaForm(forms.ModelForm):

       class Meta:
        model = models.profesor_materia
        fields = "__all__"

        widgets = {
            "profesor": forms.Select(attrs={"class": "form-control"}),
            "materia": forms.Select(attrs={"class": "form-control"}),
            "nivel": forms.Select(attrs={"class": "form-control"}),
        }