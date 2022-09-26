from rest_framework.viewsets import ModelViewSet
from modules.user.models import customUser as User
from modules.user.serializers import UserSerializer
from modules.course.permissions import IsAdminOrReadyOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly



# Create your views here.
class UsersViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadyOnly]