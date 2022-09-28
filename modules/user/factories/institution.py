import factory
from factory.django import DjangoModelFactory
from random import randint
from modules.user.models import Institution
from factory import Faker, SubFactory


class InstitutionFactory(DjangoModelFactory):
    
    class Meta:
        model=Institution

    name = Faker("company")




