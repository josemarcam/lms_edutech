from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.exam.factories.exam import ExamFactory
from modules.exam.factories.exercise import ExerciseFactory
from modules.exam.models import Exercise
from modules.exam.views import ExerciseViews


from modules.user.factories.institution import InstitutionFactory
from modules.user.models import CustomUser as User

class ExerciseTestCase(TestCase):

    def test_create_exercise(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        exam = ExamFactory(institution=institution)

        payload = {
            "statement": "lesson testt",
            "answer": 1,
            "alternatives": {"options": ["batata", "cebola", "acelga"]},
            "exam": exam.id
        }


        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        view = ExerciseViews.as_view({"post": "create"})

        request = factory.post('/exercises/', data=payload, format="json")
        
        force_authenticate(request, user=user)
        response = view(request)
        exercise_count = Exercise.objects.all().count()
        # print(response.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(exercise_count, 1)


    def test_create_exercise_not_auth(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        exam = ExamFactory(institution=institution)

        payload = {
            "statement": "lesson testt",
            "answer": 1,
            "alternatives": {"options": ["batata", "cebola", "acelga"]},
            "exam": exam.id
        }

        view = ExerciseViews.as_view({"post": "create"})

        request = factory.post('/exercises/', data=payload, format="json")
        
        
        force_authenticate(request)
        response = view(request)

        self.assertEqual(response.status_code, 401)

    def test_retrieve_exercise(self):
        
        factory = APIRequestFactory()
        institution = InstitutionFactory()
        exam = ExamFactory(institution=institution)
        exercise = ExerciseFactory(exam=exam)
        
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        view = ExerciseViews.as_view({"get": "retrieve"})

        request = factory.get('/exercises/')
        force_authenticate(request, user=user)

        response = view(request, pk=exercise.id)
        # print(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], exercise.id)