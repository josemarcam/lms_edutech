from factory.django import DjangoModelFactory
from factory import Faker
from random import randint
from modules.course.models import Discipline


class DisciplineFactory(DjangoModelFactory):
    
    class Meta:
        model=Discipline

    name = Faker("first_name")
    workload = randint(10,45)
    description = Faker("paragraph")
    