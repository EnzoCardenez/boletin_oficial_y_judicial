from django.db import models

# Create your models here.


class Organismo(models.Model):

    nombre = models.CharField(max_length=350, blank=False, null=False)
    cuit = models.PositiveIntegerField(blank=False, null=False)
    descripcion = models.TextField(max_length=600, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Organismo: {self.nombre}'
