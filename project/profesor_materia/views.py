from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import forms, models


class profesorList(ListView):
    model = models.profesor_materia


    

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.profesor_materia.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.profesor_materia.objects.all()
        return object_list



class profesor_materiaCreate(CreateView):
    model = models.profesor_materia
    form_class = forms.profesor_materiaForm
    success_url = reverse_lazy("profesor:profesor_list")


class profesor_materiaUpdate(UpdateView):
    model = models.profesor_materia
    form_class = forms.profesor_materiaForm
    success_url = reverse_lazy("profesor:profesor_list")