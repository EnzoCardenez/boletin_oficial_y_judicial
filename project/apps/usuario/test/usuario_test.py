import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from core.tests.utils import get
from usuario.test.factories import UsuarioFactory


Usuario = get_user_model()


@pytest.mark.django_db
def test_usuario():
    usuario_instance = UsuarioFactory.create()

    usuario_db = Usuario.objects.get(pk=usuario_instance.id)

    assert usuario_instance.first_name == usuario_db.first_name
    assert usuario_instance.last_name == usuario_db.last_name
    assert usuario_instance.username == usuario_db.username


@pytest.mark.django_db
def test_usuario_list():
    usuario = UsuarioFactory.create(username='pytest_wacho_pistola',  is_superuser=True)

    endpoint = reverse(viewname='usuario-list')

    response = get(url=f'{endpoint}', user_logged=usuario)

    assert response.status_code == 200
    assert response.json()['meta']['pagination']['count'] == 1


@pytest.mark.django_db
@pytest.mark.parametrize('superadmin, id, assert_id', [(True, 2, '2'), (False, 2, '1')])
def test_usuario_retrive(superadmin, id, assert_id):

    usuario_admin = UsuarioFactory.create(
        username='pytest_el_polenta',
        email='pytest_perico@email.com',
        is_superuser=superadmin,
    )
    UsuarioFactory.create(
        username='pytest_no_tan_polenta',
        email='pytest_vaca@email.com',

    )

    endpoint = reverse(viewname='usuario-detail', kwargs={'pk': id}, )
    response = get(url=f'{endpoint}', user_logged=usuario_admin)

    assert response.status_code == 200
    assert response.json()['data']['id'] == assert_id


'''En el siguiente test establecemos los parametros de la consulta
luego creamos nuevas instancias la factoria de usuario en relacion a los datos establecidos en el parametrize
Declaramos una nueva variable que ademas de tomar de la factoria, va a tomar de estas nuevas instancias 
IMPORTANTE: el test es de filtros, por lo que en la url deberemos agregar el query_params'''


@pytest.mark.django_db
@pytest.mark.parametrize('query_params, count', [
    ('?es_boletin=True', 2),
    ('?es_boletin=False', 3),
    ('?Filtro=ecardenez', 1),
    ('?Filtro=marcos', 1),
    ('?Filtro=polo', 1)
])
def test_usuario_filtro(query_params, count):
    UsuarioFactory.create_batch(es_boletin=False, size=3)
    UsuarioFactory.create(username='ecardenez', es_boletin=True, first_name='marcos', last_name='polo')
    usuario = UsuarioFactory.create(es_boletin=True, is_superuser=True)

    endpoint = reverse(viewname='usuario-list')
    response = get(url=f'{endpoint}{query_params}', user_logged=usuario)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['meta']['pagination']['count'] == count
