from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "clase_particular"

urlpatterns = [
    
     path("", TemplateView.as_view(template_name="alumno/index.html"), name="index"),
]