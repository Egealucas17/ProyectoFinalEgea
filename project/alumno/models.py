from django.db import models 
from year import models as m




class alumno(models.Model):

    nombre = models.CharField(max_length=40)
    escuela = models.CharField(max_length=20)
    anio = models.ForeignKey(m.year, on_delete= models.SET_NULL, null= "True", blank= "True")
    
    
    def __str__(self):
        return f"{self.nombre}"

