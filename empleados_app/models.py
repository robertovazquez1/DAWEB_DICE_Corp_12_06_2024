from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=50)
    apellido=models.CharField( max_length=50)
    telefono=models.IntegerField()
    salario=models.FloatField()
    genero=models.CharField(max_length=50)
    puesto=models.CharField( max_length=50)
    def __str__(self):
        return self.nombre