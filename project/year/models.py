from django.db import models
from nivel import models as m



class year (models.Model):

    anio = models.IntegerField()
    nivel= models.ForeignKey(m.nivel, on_delete= models.SET_NULL, null= "True", blank= "True")

    def __str__(self) -> str:
        return f"{self.anio}° de {self.nivel.descripcion} "
    

    
