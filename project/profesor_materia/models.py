from django.db import models 
from nivel import models as modelosnivel
from profesor import models as modelosProf
from materia import models as modelosMat




class profesor_materia(models.Model):

    profesor = models.ForeignKey(modelosProf.profesor, on_delete= models.SET_NULL, null= "True", blank= "True")
    materia = models.ForeignKey(modelosMat.materia, on_delete= models.SET_NULL, null= "True", blank= "True")
    nivel = models.ForeignKey(modelosnivel.nivel, on_delete= models.SET_NULL, null= "True", blank= "True", )
    
    
    def __str__(self):
        return f"{self.materia.descripcion} del nivel {self.nivel.descripcion} dictada por {self.profesor.nombre} "

