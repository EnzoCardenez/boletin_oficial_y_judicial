from django.db import models
from django.core.validators import FileExtensionValidator

from usuario.models import Usuario
from .constant import ESTADO

import uuid
# Create your models here.


class Fecha(models.Model):
    class Meta:
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'

    fechas_a_publicar = models.DateField()

    def __str__(self):
        return f'fecha: {self.pk}'


class Publicacion(models.Model):

    class Meta:

        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    uuid = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    estado = models.CharField(max_length=23, choices=ESTADO, default='iniciado')
    cuerpo_publicacion = models.TextField(max_length=5500, blank=False, null=False)
    palabras = models.BigIntegerField(editable=False)
    dias_de_publicacion = models.IntegerField(blank=False, null=False)
    sellos = models.IntegerField(blank=False, null=False)
    copias_requeridas = models.BooleanField(blank=False, null=False, default=False)
    cantidad_de_copias = models.IntegerField(editable=False)
    cuil = models.IntegerField(blank=True, null=True)
    creado_por = models.ForeignKey(
                                    Usuario,
                                    on_delete=models.CASCADE,
                                    related_name='create_publicacion',
                                    editable=False,
                                    )
    modificado_por = models.ForeignKey(
                                        Usuario,
                                        on_delete=models.CASCADE,
                                        related_name='update_publicacion',
                                        editable=False,
                                        )
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_publicacion = models.ForeignKey(Fecha, on_delete=models.CASCADE, blank=True, null=True)
    archivo = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return f'publicacion N°: {self.pk}'
