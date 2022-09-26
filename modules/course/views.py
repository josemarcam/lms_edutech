from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from modules.course.models import (
    Discipline,
    Module,
    Lesson,
    Course
)
from modules.course.permissions import IsAdminOrReadyOnly
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
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadyOnly]

class DisciplineViews(ModelViewSet):
    """
    List all disciplines, or create a new discipline.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ModuleViews(ModelViewSet):
    """
    List all modules, or create a new module.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LessonViews(ModelViewSet):
    """
    List all Lessons, or create a new lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]