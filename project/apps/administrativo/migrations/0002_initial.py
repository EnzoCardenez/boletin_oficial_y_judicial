# Generated by Django 5.0 on 2024-01-03 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrativo', '0001_initial'),
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='publicacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='publicacion.publicacion'),
        ),
    ]