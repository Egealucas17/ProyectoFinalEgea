from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "alumno"

urlpatterns = [
    
     path("", TemplateView.as_view(template_name="alumno/index.html"), name="index"),
]


urlpatterns += [

    path("alumno/list/", views.alumnoList.as_view(), name="alumno_list"),
    path("alumno/create/", views.alumnoCreate.as_view(), name="alumno_create"),
    path("alumno/detail/<int:pk>", views.alumnoDetail.as_view(), name="alumno_detail"),
    path("alumno/update/<int:pk>", views.alumnoUpdate.as_view(), name="alumno_update"),
    path("alumno/delete/<int:pk>", views.alumnoDelete.as_view(), name="alumno_delete"),
    
]


