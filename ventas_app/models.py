from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.IntegerField(primary_key=True)
    id_empleado=models.IntegerField()
    id_cliente=models.IntegerField()
    id_articulo=models.IntegerField()
    id_local=models.IntegerField()
    cantidad_compra=models.IntegerField()
    metodo_pago=models.CharField( max_length=50)
    total=models.FloatField()
    