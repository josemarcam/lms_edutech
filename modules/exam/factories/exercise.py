from random import randint
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory, RelatedFactory, Dict

from modules.exam.models import Exercise
from modules.user.factories.course_class import CourseClassFactory
from modules.user.factories.institution import InstitutionFactory

class ExerciseFactory(DjangoModelFactory):
    
    class Meta:
        model=Exercise

    statement = Faker("paragraph")
    answer = randint(1,3)
    alternatives = Dict({"options": ["batata", "cebola", "acelga"]})
    exam = None