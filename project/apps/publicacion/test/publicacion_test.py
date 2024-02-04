import pytest
import os

from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.conf import settings


from .factories import FechaFactory, PublicacionFactory
from usuario.test.factories import UsuarioFactory

from publicacion.count import palabra, copias
from publicacion.constant import (
    INICIADO,
    PENDIENTE_PAGO,
    PENDIENTE_REVISION_PAGO,
    APROBADO,
    RECHAZADO,
)

test_media = os.path.join(settings.MEDIA_ROOT)


@pytest.mark.django_db
def test_publicacion_post():
    usuario = UsuarioFactory.create(is_superuser=True, es_boletin=True)

    client = APIClient()
    client.force_authenticate(user=usuario)

    cuerpo_publicacion = 'somos los trobadores, estamos todos locos de atar'
    copias_requeridas = True
    dias = 2

    _field = SimpleUploadedFile(name='pytest.pdf',
                                content=open(f'{test_media}/test_files/pytest.pdf', 'rb').read(),
                                content_type='application/pdf',)

    data = {
        'estado': INICIADO,
        'cuerpo_publicacion': cuerpo_publicacion,
        'palabras': palabra(cuerpo_publicacion),
        'sellos': 1,
        'dias_a_publicar': copias_requeridas,
        'copias_requeridas': dias,
        'cantidad_de_copias': copias(dias, copias_requeridas),
        'archivo': _field

    }

    endpoint = reverse(viewname='publicacion-list')
    response = client.post(path=endpoint, data=data, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
