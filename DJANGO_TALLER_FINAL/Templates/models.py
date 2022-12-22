from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    fono = models.CharField(max_length=15, null=False)
    fecha_inscripcion = models.DateField(null=False)
    institucion = models.CharField(max_length=30,null=False)
    hora_inscripcion = models.CharField(max_length=5, null=False)
    estado = models.CharField(max_length=20, null=False)
    observacion = models.CharField(max_length=40)
