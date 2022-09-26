from django.test import TestCase
from modules.user.models import customUser as User
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.course.factories.discipline import DisciplineFactory
from modules.course.models import (
    Discipline,
    Lesson
)
from modules.course.views import (
    DisciplineViews
)


class DisciplineTestCase(TestCase):

    def test_create_discipline(self):
        
        factory = APIRequestFactory()
        user = User.objects.create_user('username', 'Pas$w0rd')
        payload = {
            "name": "lesson testt",
            "workload": 40,
            "description": "esse é só um test",
            "professor": user.username
        }


        view = DisciplineViews.as_view({"post": "create"})

        request = factory.post('/disciplines/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        discipline_count = Discipline.objects.all().count()
        # print(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(discipline_count, 1)
    
    def test_create_discipline_not_auth(self):
        
        factory = APIRequestFactory()
        payload = {
            "name": "lesson testt",
            "workload": 40,
            "description": "esse é só um test",
        }

        view = DisciplineViews.as_view({"post": "create"})

        request = factory.post('/disciplines/', data=payload, format="json")
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 403)

    def test_update_discipline(self):
        
        factory = APIRequestFactory()
        discipline = DisciplineFactory()
        user = User.objects.create_user('username', 'Pas$w0rd')
        # print(f"nome do bagulho -> {discipline.name}")
         
        payload = {
            "id": discipline.id,
            "name": "lesson testt",
            "workload": 40,
            "description": "esse é só um test",
            "professor": None
        }

        view = DisciplineViews.as_view({"put": "update"})

        request = factory.put(f'/disciplines/{discipline.id}', data=payload, format="json")
        
        force_authenticate(request, user=user)
        response = view(request, pk=discipline.id)
        discipline_updated = Discipline.objects.all()
        
        # print(response.data)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(discipline_updated[0].name, payload["name"])
        self.assertEqual(str(discipline_updated[0]), discipline_updated[0].name)