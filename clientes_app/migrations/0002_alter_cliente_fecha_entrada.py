# Generated by Django 5.1.3 on 2024-12-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_entrada',
            field=models.CharField(max_length=50),
        ),
    ]
