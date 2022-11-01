from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory
from modules.course.factories.course import CourseFactory
from modules.course.views import CourseViews
from modules.user.factories.course_class import CourseClassFactory


from modules.user.factories.institution import InstitutionFactory
from modules.user.models import CustomUser as User
from modules.user.views import CourseClassViews

class IsAdminOrReadyOnlyTestCase(TestCase):

    def test_is_admin_or_read_only(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course = CourseFactory(institution=institution)

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[0][0])

        view = CourseViews.as_view({"get": "retrieve"})

        request = factory.get('/course/')
        
        force_authenticate(request, user=user)
        response = view(request,pk=course.id)
        # print(response.data)

        self.assertEqual(response.status_code, 200)
    
    def test_post_as_user_level_not_allowed(self):

        factory = APIRequestFactory()
        payload = {
            "name": "lesson testt",
            "description": "esse é só um test",
            "studants": [],
            "disciplines": [],
        }

        institution = InstitutionFactory()

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[1][0])

        view = CourseViews.as_view({"post": "create"})

        request = factory.post('/courses/', data=payload, format="json")
        
        
        force_authenticate(request, user=user)
        response = view(request)
        # print(response.data)
        
        self.assertEqual(response.status_code, 403)


class AtLeastProfessorOrClassCoursePermissionTestCase(TestCase):

    def test_is_admin(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course_class = CourseClassFactory(institution=institution)

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[0][0])

        view = CourseClassViews.as_view({"get": "retrieve"})

        request = factory.get('/course-class/')
        
        force_authenticate(request, user=user)
        response = view(request,pk=course_class.id)
        # print(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(course_class.name, course_class.__str__())
    
    def test_studant_access_not_allowed(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        course_class = CourseClassFactory(institution=institution)

        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[2][0])

        view = CourseClassViews.as_view({"get": "retrieve"})

        request = factory.get('/course-class/')
        
        force_authenticate(request, user=user)
        response = view(request,pk=course_class.id)
        # print(response.data)

        self.assertEqual(response.status_code, 403)
    
    def test_studant_access_allowed(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[2][0])
        
        course_class = CourseClassFactory(institution=institution,studants=[user])


        view = CourseClassViews.as_view({"get": "retrieve"})

        request = factory.get('/course-class/')
        
        force_authenticate(request, user=user)
        response = view(request,pk=course_class.id)
        # print(response.data)

        self.assertEqual(response.status_code, 200)
    
    def test_not_auth_access(self):

        factory = APIRequestFactory()
        institution = InstitutionFactory()
        user = User.objects.create_user('username', 'Pas$w0rd', institution=institution, user_level=User.USER_LEVEL[2][0])
        
        course_class = CourseClassFactory(institution=institution,studants=[user])


        view = CourseClassViews.as_view({"get": "retrieve"})

        request = factory.get('/course-class/')
        
        response = view(request,pk=course_class.id)
        # print(response.data)

        self.assertEqual(response.status_code, 403)