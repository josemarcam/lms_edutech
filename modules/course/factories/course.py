import factory
from factory.django import DjangoModelFactory
from random import randint
from modules.course.models import Course
from factory import Faker


class CourseFactory(DjangoModelFactory):
    
    class Meta:
        model=Course

    name = "trest"
    description = Faker("paragraph")

    @factory.post_generation
    def disciplines(self, create, extracted, **kwargs):
        if extracted:
            for discipline in extracted:
                self.disciplines.add(discipline)
        
        if not extracted:
            qtd = randint(1, 3)
    
    @factory.post_generation
    def studants(self, create, extracted, **kwargs):
        if extracted:
            for studant in extracted:
                self.studants.add(studant)
        
        if not extracted:
            qtd = randint(1, 3)




