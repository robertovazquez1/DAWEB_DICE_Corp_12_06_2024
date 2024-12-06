from django.db import models

# Create your models here.
class Membresia(models.Model):
    id_membresia=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=250)
    cantidad=models.IntegerField()
    tiempo_vigen=models.CharField( max_length=50)
    precio_membre=models.FloatField()
    descuento=models.IntegerField()
    color=models.CharField( max_length=50)