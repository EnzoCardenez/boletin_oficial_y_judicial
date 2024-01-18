from django.contrib.auth.models import AbstractUser
from django.db import models

from organismo.models import Organismo

# Create your models here.


class Usuario(AbstractUser):

    class Meta:
        db_table = "auth_user"

    organismo = models.ForeignKey(Organismo, on_delete=models.SET_NULL, blank=True, null=True)
    es_boletin = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return f'usuario: {self.username}'


