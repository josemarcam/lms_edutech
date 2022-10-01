import factory
from factory.django import DjangoModelFactory
from random import randint
from modules.user.factories.institution import InstitutionFactory
from modules.user.models import CustomUser as User
from factory import Faker, SubFactory


class UserFactory(DjangoModelFactory):
    
    class Meta:
        model=User

    username = Faker("user_name")
    email = Faker("ascii_company_email")
    user_level = User.USER_LEVEL[2][0]
    institution = SubFactory(InstitutionFactory)

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
        
        if not extracted:
            self.set_password("123qwe")
            

