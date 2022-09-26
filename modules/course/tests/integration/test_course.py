from django.test import TestCase
from modules.user.models import customUser as User
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.course.factories.discipline import DisciplineFactory
from modules.course.factories.course import CourseFactory
from modules.course.models import (
    Course,
    Lesson
)
from modules.course.views import (
    CourseViews
)


class CourseTestCase(TestCase):

    def test_create_course(self):
        
        factory = APIRequestFactory()
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "studants": [],
            "disciplines": [],
        }
        user = User.objects.create_user('username', 'Pas$w0rd')

        view = CourseViews.as_view({"post": "create"})

        request = factory.post('/courses/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        course_count = Course.objects.all().count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(course_count, 1)
    
    def test_create_course_not_auth(self):
        
        factory = APIRequestFactory()
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "studants": [],
            "disciplines": [],
        }

        view = CourseViews.as_view({"post": "create"})

        request = factory.post('/courses/', data=payload, format="json")
        
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 403)
    
    def test_create_course_with_disciplines(self):
        
        factory = APIRequestFactory()
        discipline = DisciplineFactory()
         
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "studants": [],
            "disciplines": [discipline.id],
        }
        user = User.objects.create_user('username', 'Pas$w0rd')

        view = CourseViews.as_view({"post": "create"})

        request = factory.post('/courses/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        course_count = Course.objects.all().count()
        course = Course.objects.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(course_count, 1)
        self.assertEqual(course[0].disciplines.all()[0].id, discipline.id)
        
    
    def test_update_course(self):
        
        factory = APIRequestFactory()
        course = CourseFactory()
        # print(f"nome do bagulho -> {course.name}")
         
        payload = {
            "id": course.id,
            "name": "historia42",
            "description": "essa descrucai aqyu",
            "studants": [],
            "disciplines": []
        }
        user = User.objects.create_user('username', 'Pas$w0rd')

        view = CourseViews.as_view({"put": "update"})

        request = factory.put(f'/courses/{course.id}', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request, pk=course.id)
        course_updated = Course.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(course_updated[0].name, payload["name"])
        self.assertEqual(str(course_updated[0]), course_updated[0].name)