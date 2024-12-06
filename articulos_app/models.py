from django.db import models

# Create your models here.
class Articulo(models.Model):
    id_articulo=models.IntegerField(primary_key=True)
    cantidad_arti=models.IntegerField()
    nombre=models.CharField( max_length=50)
    precio=models.FloatField()
    fecha_crea=models.CharField( max_length=50)
    estado=models.CharField( max_length=50)
    color=models.CharField( max_length=50)