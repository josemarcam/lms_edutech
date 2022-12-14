from django.test import TestCase
from modules.course.factories.course import CourseFactory
from modules.user.factories.institution import InstitutionFactory
from modules.user.models import CustomUser as User
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.course.factories.discipline import DisciplineFactory
from modules.course.factories.module import ModuleFactory
from modules.course.models import (
    Module
)
from modules.course.views import (
    ModuleViews
)


class ModuleTestCase(TestCase):

    def test_create_module(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course = CourseFactory(institution=institution)
        discipline = DisciplineFactory(courses=[course])

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution)

        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "discipline": discipline.id
        }

        view = ModuleViews.as_view({"post": "create"})

        request = factory.post('/modules/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        module_count = Module.objects.all().count()
        # print(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(module_count, 1)
    
    def test_create_module_not_auth(self):
        
        factory = APIRequestFactory()
        discipline = DisciplineFactory()
        
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "discipline": discipline.id
        }

        view = ModuleViews.as_view({"post": "create"})

        request = factory.post('/modules/', data=payload, format="json")
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 401)

    def test_update_module(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course = CourseFactory(institution=institution)
        discipline = DisciplineFactory(courses=[course])
        module = ModuleFactory(discipline=discipline)

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution)
        
        # print(f"nome do bagulho -> {module.name}")
         
        payload = {
            "id": module.id,
            "name": "lesson testt",
            "description": "esse é só um test",
            "discipline": discipline.id
        }

        view = ModuleViews.as_view({"put": "update"})

        request = factory.put(f'/modules/{module.id}', data=payload, format="json")
        
        force_authenticate(request, user=user)
        response = view(request, pk=module.id)
        module_updated = Module.objects.all()
        
        # print(response.data)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(module_updated[0].name, payload["name"])
        self.assertEqual(str(module_updated[0]), module_updated[0].name)