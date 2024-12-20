# Generated by Django 5.1.3 on 2024-12-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('salario', models.FloatField()),
                ('genero', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
            ],
        ),
    ]
