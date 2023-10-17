from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "profesor_materia"

urlpatterns = [
     path("profesor_materia/list/", views.profesorList.as_view(), name="profesor_materia_list"),
     path("profesor_materia/create", views.profesor_materiaCreate.as_view(), name="profesor_materia_create"),
     path("profesor_materia/update/<int:pk>", views.profesor_materiaUpdate.as_view(), name="profesor_materia_update")
]