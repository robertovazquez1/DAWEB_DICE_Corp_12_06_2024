from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.IntegerField(primary_key=True)
    fecha_entrada=models.CharField( max_length=50)
    tiempo_local=models.CharField( max_length=50)
    compra=models.CharField( max_length=50)
    id_membresia=models.CharField(default='si', max_length=50)
    metodo_pago=models.CharField( max_length=50)
    calificacion_dada=models.CharField( max_length=50)
    def __str__(self):
        return self.fecha_entrada