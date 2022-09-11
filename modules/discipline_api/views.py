from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from modules.discipline_api.models import (
    Discipline,
    Module,
    Lesson
)
from modules.discipline_api.serializers import (
    DisciplineSerializer,
    ModuleSerializer,
    LessonSerializer
)

class DisciplineViews(ModelViewSet):
    """
    List all disciplines, or create a new discipline.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ModuleViews(ModelViewSet):
    """
    List all modules, or create a new module.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LessonViews(ModelViewSet):
    """
    List all Lessons, or create a new lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
