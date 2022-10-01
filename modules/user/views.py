from rest_framework.viewsets import ModelViewSet
from modules.user.models import CourseClass, CustomUser as User, Institution
from modules.user.serializers import CourseClassSerializer, InstitutionSerializer, UserSerializer
from modules.shared.permissions.custom_permission import AtLeastProfessorPermission, IsAdminOrReadyOnly
from rest_framework.permissions import IsAdminUser


class UserViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadyOnly]

class InstitutionViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAdminUser]

class CourseClassViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    # queryset = Course.objects.all()
    serializer_class = CourseClassSerializer
    permission_classes = [AtLeastProfessorPermission]

    def get_queryset(self):
        return CourseClass.objects.filter(institution = self.request.user.institution.id)

    def perform_create(self, serializer):
        serializer.save(institution=self.request.user.institution)
    