# Generated by Django 5.1.3 on 2024-12-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('id_empleado', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('id_articulo', models.IntegerField()),
                ('id_local', models.IntegerField()),
                ('cantidad_compra', models.IntegerField()),
                ('metodo_pago', models.CharField(max_length=50)),
                ('total', models.FloatField()),
            ],
        ),
    ]
