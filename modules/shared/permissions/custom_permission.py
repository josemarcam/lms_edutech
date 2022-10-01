from rest_framework.permissions import BasePermission, SAFE_METHODS
from modules.user.models import CustomUser

class IsAdminOrReadyOnly(BasePermission):

    def has_permission(self, request, view):
        
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True
        
        if int(request.user.user_level) == int(CustomUser.USER_LEVEL[0][0]):
            return True
        
        return False

class AtLeastProfessorPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.user and request.user.is_authenticated:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):

        user = request.user

        if int(request.user.user_level) <= int(CustomUser.USER_LEVEL[1][0]):
            return True
        course_class = getattr(obj,"course_class",obj)
        return course_class.user_is_in_class(user.id)