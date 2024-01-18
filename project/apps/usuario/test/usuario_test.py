from unittest import TestCase

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from usuario.test.factories import UsuarioFactory
from usuario.serializers import UsuarioSerializer

User = get_user_model()


@pytest.mark.django_db
def usuario_test():
    usuario = UsuarioFactory.create(last_name='Cardenez', firts_name='Enzo', username='ecardenez', es_boletin=False)
    serializer = UsuarioSerializer()
    serializer.get_user_permissions(instance=usuario)
    assert usuario.__str__() == usuario.username
