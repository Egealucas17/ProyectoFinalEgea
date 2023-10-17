from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "profesor"

urlpatterns = [
    
     path("", TemplateView.as_view(template_name="profesor/index.html"), name="index"),
]


urlpatterns += [

    path("profesor/list/", views.profesorList.as_view(), name="profesor_list"),
    path("profesor/create/", views.profesorCreate.as_view(), name="profesor_create"),
    path("profesor/detail/<int:pk>", views.profesorDetail.as_view(), name="profesor_detail"),
    path("profesor/update/<int:pk>", views.profesorUpdate.as_view(), name="profesor_update"),
    path("profesor/delete/<int:pk>", views.profesorDelete.as_view(), name="profesor_delete"),
    
]


