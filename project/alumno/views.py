from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from . import forms, models



class alumnoList(ListView):
    model = models.alumno

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.alumno.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.alumno.objects.all()
        return object_list



class alumnoCreate(CreateView):
    model = models.alumno
    form_class = forms.AlumnoForm
    success_url = reverse_lazy("alumno:alumno_list")


class alumnoDetail(DetailView):
    model = models.alumno


class alumnoUpdate(UpdateView):
    model = models.alumno
    form_class = forms.AlumnoForm
    success_url = reverse_lazy("alumno:alumno_list")


class alumnoDelete(DeleteView):
    model = models.alumno
    success_url = reverse_lazy("alumno:alumno_list")

