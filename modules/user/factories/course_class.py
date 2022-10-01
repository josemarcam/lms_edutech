import factory
from factory.django import DjangoModelFactory
from random import randint
from modules.user.factories.institution import InstitutionFactory
from modules.user.factories.user import UserFactory
from modules.user.models import CourseClass, CustomUser as User
from factory import Faker, SubFactory, List, RelatedFactory, SelfAttribute


class CourseClassFactory(DjangoModelFactory):
    
    class Meta:
        model=CourseClass

    name = Faker("user_name")
    institution = SubFactory(InstitutionFactory)

    @factory.post_generation
    def studants(self, create, extracted, **kwargs):
        if extracted:
            for discipline in extracted:
                self.studants.add(discipline)
        
        if not extracted:
            for _ in range(randint(1, 3)):
                studant = UserFactory(institution = self.institution)
                self.studants.add(studant)

