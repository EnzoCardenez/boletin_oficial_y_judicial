import factory
from factory import django, faker, SubFactory, SelfAttribute

from publicacion.models import Publicacion, Fecha
from usuario.test.factories import UsuarioFactory


class FechaFactory(django.DjangoModelFactory):
    class Meta:
        model = Fecha

    fecha_a_publicar = factory.Faker(provider='random_digit')


class PublicacionFactory(django.DjangoModelFactory):

    class Meta:
        model = Publicacion

    cuerpo_publicacion = faker.Faker(provider='sentence', nb_words=16)
    dias_de_publicacion = faker.Faker(provider='random_digit')
    cantidad_de_copias = 0
    creado_por = SubFactory(UsuarioFactory)
    modificado_por = SelfAttribute(attribute_name='creado_por')

