from django.db import models


class materia (models.Model):

    descripcion = models.CharField(max_length= 30)
    

    def __str__(self) -> str:
        return f"{self.descripcion} "
    

    
