from rest_framework.viewsets import ModelViewSet
from modules.user.models import CustomUser as User, Institution
from modules.user.serializers import InstitutionSerializer, UserSerializer
from modules.shared.permissions.custom_permission import IsAdminOrReadyOnly
from rest_framework.permissions import IsAdminUser



# Create your views here.
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