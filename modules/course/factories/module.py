from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from random import randint
from modules.course.models import Module
from modules.course.factories.discipline import DisciplineFactory


class ModuleFactory(DjangoModelFactory):
    
    class Meta:
        model=Module

    name = Faker("first_name")
    description = Faker("paragraph")
    discipline = SubFactory(DisciplineFactory)
