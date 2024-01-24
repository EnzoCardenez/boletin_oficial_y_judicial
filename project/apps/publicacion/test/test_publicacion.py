import pytest
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import UploadedFile
from rest_framework.test import APIClient

from .factories import FechaFactory, PublicacionFactory
from usuario.test.factories import UsuarioFactory

from publicacion.count import palabra, copias


@pytest.mark.django_db
def test_publicacion_post():
    user = UsuarioFactory.create()
    publicacion = PublicacionFactory.create()

