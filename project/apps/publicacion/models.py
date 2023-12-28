from django.db import models

from .constant import ESTADO

# Create your models here.


class Publicacion(models.Model):

    class Meta:

        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

        uuid = models.UUIDField(primary_key=False)
        estado = models.CharField(choices=ESTADO)
        cuerpo_publicacion = models.TextField(max_length=5500, blank=False, null=False)
        palabras = models.BigIntegerField(editable=False)
        dias_de_publicacion = models.IntegerField(max_length=7)
        sellos = models.IntegerField(max_length=2)
        cuil = models.IntegerField(max_length=11)
        fecha_creacion = models.DateField(auto_now_add=True)
        fecha_modificacion = models.DateField(auto_now=True)
        fecha_publicacion = models.Many
        archivo = models.FileField()






