from django.db import models



class year (models.Model):

    anio = models.IntegerField()
    nivel= models.CharField(max_length = 10)

    def __str__(self) -> str:
        return f"{self.anio}° de {self.nivel} "
    

    
