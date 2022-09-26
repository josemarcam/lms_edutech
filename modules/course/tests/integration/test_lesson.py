from django.test import TestCase
from modules.user.models import CustomUser as User
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.course.factories.module import ModuleFactory
from modules.course.factories.lesson import LessonFactory
from modules.course.models import (
    Lesson
)
from modules.course.views import (
    LessonViews
)


class LessonTestCase(TestCase):

    def test_create_lesson(self):
        
        factory = APIRequestFactory()
        user = User.objects.create_user('username', 'Pas$w0rd')
        module = ModuleFactory()

        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "module": module.id
        }

        view = LessonViews.as_view({"post": "create"})

        request = factory.post('/lessons/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        lesson_count = Lesson.objects.all().count()
        # print(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(lesson_count, 1)
    
    def test_create_lesson_not_auth(self):
        
        factory = APIRequestFactory()
        module = ModuleFactory()
        
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "module": module.id
        }

        view = LessonViews.as_view({"post": "create"})

        request = factory.post('/lessons/', data=payload, format="json")
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 403)

    def test_update_lesson(self):
        
        factory = APIRequestFactory()
        lesson = LessonFactory()
        user = User.objects.create_user('username', 'Pas$w0rd')
        
        # print(f"nome do bagulho -> {lesson.name}")
         
        payload = {
            "id": lesson.id,
            "name": "lesson testt",
            "description": "esse é só um test",
            "module": None
        }

        view = LessonViews.as_view({"put": "update"})

        request = factory.put(f'/lessons/{lesson.id}', data=payload, format="json")
        
        force_authenticate(request, user=user)
        response = view(request, pk=lesson.id)
        lesson_updated = Lesson.objects.all()
        
        # print(response.data)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(lesson_updated[0].name, payload["name"])
        self.assertEqual(str(lesson_updated[0]), lesson_updated[0].name)