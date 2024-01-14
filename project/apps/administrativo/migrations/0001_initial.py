# Generated by Django 5.0 on 2024-01-03 20:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('descuento', models.FloatField()),
                ('total', models.FloatField()),
            ],
            options={
                'verbose_name': 'Abonado',
                'verbose_name_plural': 'Abonados',
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_comprobante', models.CharField(max_length=15)),
                ('archivo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('precio_por_palabra', models.FloatField()),
                ('precio_por_ejemplar', models.FloatField()),
                ('vigencia_desde', models.DateField()),
                ('vigencia_hasta', models.DateField()),
                ('activo', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name': 'Precio',
                'verbose_name_plural': 'Precios',
            },
        ),
    ]