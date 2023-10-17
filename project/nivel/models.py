from django.db import models


class nivel(models.Model):

    descripcion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.descripcion}"
