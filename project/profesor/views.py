from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from . import forms, models



class profesorList(ListView):
    model = models.profesor

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.profesor.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.profesor.objects.all()
        return object_list



class profesorCreate(CreateView):
    model = models.profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy("profesor:profesor_list")


class profesorDetail(DetailView):
    model = models.profesor


class profesorUpdate(UpdateView):
    model = models.profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy("profesor:profesor_list")


class profesorDelete(DeleteView):
    model = models.profesor
    success_url = reverse_lazy("profesor:profesor_list")

