from factory import django, SubFactory, faker


from usuario.models import Usuario


class UsuarioFactory(django.DjangoModelFactory):
    class Meta:
        models = Usuario

    username = faker.Faker(provider='user_name')
    organismo = SubFactory(factory=OrganismoFactory)
    es_boletin = False
    is_active = True
    