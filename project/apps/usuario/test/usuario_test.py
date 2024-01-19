from unittest import TestCase

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from usuario.test.factories import UsuarioFactory
from usuario.serializers import UsuarioSerializer

Usuario = get_user_model()


@pytest.mark.django_db
def test_usuario():
    usuario_instance = UsuarioFactory.create()

    usuario_db = Usuario.objects.get(pk=usuario_instance.id)

    assert usuario_instance.first_name == usuario_db.first_name
    assert usuario_instance.last_name == usuario_db.last_name
    assert usuario_instance.username == usuario_db.username

# def test_usuario_get():

