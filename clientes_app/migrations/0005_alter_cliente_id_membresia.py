# Generated by Django 5.1.3 on 2024-12-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0004_alter_cliente_id_membresia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_membresia',
            field=models.IntegerField(default=9),
        ),
    ]
