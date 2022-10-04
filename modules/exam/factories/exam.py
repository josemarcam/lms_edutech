import factory
from factory.django import DjangoModelFactory
from factory import SubFactory

from modules.exam.models import Exam
from modules.user.factories.course_class import CourseClassFactory
from modules.user.factories.institution import InstitutionFactory

class ExamFactory(DjangoModelFactory):
    
    class Meta:
        model=Exam

    exam_id = None
    institution = SubFactory(InstitutionFactory)
    course_class = SubFactory(CourseClassFactory, institution=institution)