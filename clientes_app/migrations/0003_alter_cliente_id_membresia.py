# Generated by Django 5.1.3 on 2024-12-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0002_alter_cliente_fecha_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_membresia',
            field=models.CharField(max_length=50),
        ),
    ]
