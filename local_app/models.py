from django.db import models

# Create your models here.
class Local(models.Model):
    id_local=models.IntegerField(primary_key=True)
    ubicacion=models.CharField( max_length=250)
    anos_funcio=models.IntegerField()
    horario=models.CharField( max_length=50)
    tamano=models.CharField( max_length=50)
    dueno=models.CharField( max_length=150)
    empleados_total=models.IntegerField()
    