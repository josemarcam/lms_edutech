from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.exam.factories.exam import ExamFactory
from modules.exam.factories.exercise import ExerciseFactory
from modules.exam.models import Exam, Exercise
from modules.exam.views import ExamViews, ExerciseViews
from modules.user.factories.course_class import CourseClassFactory


from modules.user.factories.institution import InstitutionFactory
from modules.user.models import CustomUser as User

class ExamTestCase(TestCase):

    def test_create_exam(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course_class = CourseClassFactory(institution=institution)

        payload = {
            "course_class": course_class.id,
            "exam_id": None,
            "institution": institution.id,
            "exercises": []
        }


        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        view = ExamViews.as_view({"post": "create"})

        request = factory.post('/exams/', data=payload, format="json")
        
        force_authenticate(request, user=user)
        response = view(request)
        exam_count = Exam.objects.all().count()
        # print(response.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(exam_count, 1)

    def test_create_exam_not_auth(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course_class = CourseClassFactory(institution=institution)

        payload = {
            "course_class": course_class.id,
            "exam_id": None,
            "institution": institution.id,
            "exercises": []
        }

        view = ExamViews.as_view({"post": "create"})

        request = factory.post('/exams/', data=payload, format="json")
        
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 403)
    
    def test_create_exam_with_children(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course_class = CourseClassFactory(institution=institution)
        main_exam : Exam = ExamFactory(institution=institution)
        
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        payload = {
            "course_class": course_class.id,
            "exam_id": main_exam.id,
            "institution": institution.id,
            "exercises": []
        }

        view = ExamViews.as_view({"post": "create"})

        request = factory.post('/exams/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        exam_count = Exam.objects.all().count()
        child_exam = Exam.objects.filter(id=response.data["id"]).first()
        # print(response.data)
        random_exam = main_exam.get_random_child()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(exam_count, 2)
        self.assertIsInstance(random_exam, Exam)
    
    def test_retrieve_exam(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        exam = ExamFactory(institution=institution)
        
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        view = ExamViews.as_view({"get": "retrieve"})

        request = factory.get('/exams/')
        force_authenticate(request, user=user)

        response = view(request, pk=exam.id)
        # print(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], exam.id)
    
    def test_assign_exam(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[2][0])
        course_class = CourseClassFactory(studants=[user])
        
        exam = ExamFactory(institution=institution, course_class=course_class)

        view = ExamViews.as_view({"get": "assign"})

        request = factory.get('/exams/')
        force_authenticate(request, user=user)

        response = view(request, pk=exam.id)
        # print(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], exam.id)
    
    def test_assign_exam_not_allowed(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[2][0])
        
        exam = ExamFactory(institution=institution)

        view = ExamViews.as_view({"get": "assign"})

        request = factory.get('/exams/')
        force_authenticate(request, user=user)

        response = view(request, pk=exam.id)
        # print(response.data)
        
        self.assertEqual(response.status_code, 404)