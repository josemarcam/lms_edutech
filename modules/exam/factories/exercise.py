from random import randint
from factory.django import DjangoModelFactory
from factory import Faker, Dict

from modules.exam.models import Exercise

class ExerciseFactory(DjangoModelFactory):
    
    class Meta:
        model=Exercise

    statement = Faker("paragraph")
    answer = randint(1,3)
    alternatives = Dict({"options": ["batata", "cebola", "acelga"]})
    exam = None