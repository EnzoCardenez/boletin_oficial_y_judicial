from django.db import models

# Create your models here.


class Precio(models.Model):

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'

    precio_por_palabra = models.FloatField()
    precio_por_ejemplar = models.FloatField()
    vigencia_desde = models.DateField()
    vigencia_hasta = models.DateField()
    creado_por = models.ForeignKey()
    activo = models.BooleanField()

    def __str__(self):

        return self.id


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
    publicacion = models.OneToOneField()

    def __str__(self):

        return self.id


