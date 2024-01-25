import pytest
import os

from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

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


@pytest.mark.django_db
def test_publicacion_post():
    usuario = UsuarioFactory.create(is_superuser=True, es_boletin=True)

    client = APIClient()
    client.force_authenticate(user=usuario)

    publicacion = 'somos los trobadores, estamos todos locos de atar'
    len_publicacion = 8
    total_sellos = 1
    dias_a_publicar = 3
    copias_requeridas = True
    contenido = b'Hola, que hace?'

    field = SimpleUploadedFile('archivo.pdf', contenido)

    data = {
        'estado': INICIADO,
        'cuerpo_publicacion': publicacion,
        'palabras': palabra(publicacion),
        'sellos': total_sellos,
        'dias_a_publicar': dias_a_publicar,
        'copias_requeridas': copias_requeridas,
        'cantidad_de_copias': copias(dias_a_publicar, copias_requeridas),
        'archivo': field,
        'creado_por': usuario,
        'modificado_por': usuario,

    }

    endpoint = reverse(viewname='publicacion-list')
    print(f'endopoint: {endpoint}')
    response = client.post(path=endpoint, data=data, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['data']['attributes']['estado'] == INICIADO
    assert response.json()['data']['attributes']['cuerpo_publicacion'] == publicacion
    assert response.json()['data']['attributes']['palabras'] == len_publicacion
    assert response.json()['data']['attributes']['sellos'] == total_sellos
    assert response.json()['data']['attributes']['dias a publicar'] == dias_a_publicar
    assert response.json()['data']['attributes']['copias_requeridas'] == copias_requeridas
    assert response.json()['data']['attributes']['cantidad_de_copias'] == dias_a_publicar
    assert response.json()['data']['attributes']['archivo'] == field
    assert response.json()['data']['attributes']['creado_por'] == usuario
    assert response.json()['data']['attributes']['modificado_por'] == usuario