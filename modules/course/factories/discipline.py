import factory
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

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if extracted:
            for course in extracted:
                self.courses.add(course)
        
        if not extracted:
            qtd = randint(1, 3)
    