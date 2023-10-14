
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

app_name = "home"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),

]

urlpatterns += staticfiles_urlpatterns()