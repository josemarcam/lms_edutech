from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from random import randint
from modules.course.models import Lesson
from modules.course.factories.module import ModuleFactory


class LessonFactory(DjangoModelFactory):
    
    class Meta:
        model=Lesson

    name = Faker("first_name")
    description = Faker("paragraph")
    module = SubFactory(ModuleFactory)
