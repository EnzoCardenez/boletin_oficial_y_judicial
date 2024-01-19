from factory import faker, django


from organismo.models import Organismo


class OrganismoFactory(django.DjangoModelFactory):

    class Meta:
        model = Organismo

    nombre = faker.Faker(provider='company')
    cuit = faker.Faker(provider='random_digit')



