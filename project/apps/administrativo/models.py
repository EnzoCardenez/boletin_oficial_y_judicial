from django.db import models

from usuario.models import Usuario
from publicacion.models import Publicacion
import uuid
# Create your models here.


class Precio(models.Model):

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=False)
    precio_por_palabra = models.FloatField(blank=False, null=False)
    precio_por_ejemplar = models.FloatField(blank=False, null=False)
    vigencia_desde = models.DateField(blank=False, null=False)
    vigencia_hasta = models.DateField(blank=False, null=False)
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, editable=False)
    activo = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f'precio creado por: {self.creado_por}'


class Abonado(models.Model):

    class Meta:
        verbose_name = 'Abonado'
        verbose_name_plural = 'Abonados'

    subtotal = models.FloatField()
    descuento = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"total abonado: {self.total}"


class Comprobante(models.Model):

    codigo_comprobante = models.CharField(max_length=15)
    archivo = models.FileField()
    publicacion = models.OneToOneField(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comprobante id: {self.pk}'
