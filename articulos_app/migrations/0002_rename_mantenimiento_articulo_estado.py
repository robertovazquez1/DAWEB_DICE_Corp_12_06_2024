# Generated by Django 5.1.3 on 2024-12-06 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='mantenimiento',
            new_name='estado',
        ),
    ]