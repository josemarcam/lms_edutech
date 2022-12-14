from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from modules.course.models import (
    Discipline,
    Module,
    Lesson,
    Course
)
from modules.shared.permissions.custom_permission import IsAdminOrReadyOnly
from modules.course.serializers import (
    DisciplineSerializer,
    ModuleSerializer,
    LessonSerializer,
    CourseSerializer
)


class CourseViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadyOnly]

    def get_queryset(self):
        institution = self.request.user.institution
        print(institution)
        return Course.objects.filter(institution = self.request.user.institution.id)

    def perform_create(self, serializer):
        serializer.save(institution=self.request.user.institution)
    

class DisciplineViews(ModelViewSet):
    """
    List all disciplines, or create a new discipline.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAdminOrReadyOnly]
    
    def get_queryset(self):
        institution = self.request.user.institution
        print(institution)
        return Discipline.objects.filter(courses__institution = self.request.user.institution.id)
    
    def perform_create(self, serializer):
        serializer.save(institution=self.request.user.institution)

class ModuleViews(ModelViewSet):
    """
    List all modules, or create a new module.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminOrReadyOnly]

class LessonViews(ModelViewSet):
    """
    List all Lessons, or create a new lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadyOnly]