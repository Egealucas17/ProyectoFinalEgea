from django.db import models




class profesor (models.Model):

    nombre = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 100)
    contacto = models.EmailField()



    def __str__(self) -> str:
        return f"{self.nombre}"
    

    
