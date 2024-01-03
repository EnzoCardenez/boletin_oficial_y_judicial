# Generated by Django 5.0 on 2024-01-03 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='creado_por',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='create_publicacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.fecha'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='modificado_por',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='update_publicacion', to=settings.AUTH_USER_MODEL),
        ),
    ]
