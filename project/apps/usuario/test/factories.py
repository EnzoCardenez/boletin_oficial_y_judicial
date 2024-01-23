from factory import django, SubFactory, faker


from usuario.models import Usuario

from organismo.test.factories import OrganismoFactory


class UsuarioFactory(django.DjangoModelFactory):
    class Meta:
        model = Usuario

    first_name = 'Enzo'
    last_name = 'Cardenez'
    username = faker.Faker(provider='user_name')
    organismo = SubFactory(factory=OrganismoFactory)
    es_boletin = False
    is_active = True
    