from django.db import models
from alumno import models as modeloAlumno
from profesor_materia import models as modeloPF

class clase_particular(models.Model):
    

    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    alumno = models.ForeignKey(modeloAlumno.alumno, on_delete= models.SET_NULL, null= "True", blank= "True")
    profesor_materia = models.ForeignKey(modeloPF.profesor_materia, on_delete= models.SET_NULL, null= "True", blank= "True")
    comentarios = models.CharField(max_length= 255)

