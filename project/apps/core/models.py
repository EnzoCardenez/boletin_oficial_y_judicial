from django.db import models
from django.utils import timezone

from .querysets import PublicadoQuerySet


class Publicado(models.Model):
    class Meta:
        abstract = True

    publicado = models.DateTimeField(blank=True, null=True)

    objects = PublicadoQuerySet.as_manager()

    def publicar(self, estado=True):
        self.publicado = timezone.now() if estado else None
        self.save(update_fields=('publicado',))
