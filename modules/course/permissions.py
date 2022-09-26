from rest_framework.permissions import BasePermission, SAFE_METHODS
from modules.user.models import customUser

class IsAdminOrReadyOnly(BasePermission):

    EDIT_METHODS = ("POST", "PUT", "")

    def has_permission(self, request, view):
        # print(f"{request.user.user_level == customUser.USER_LEVEL[0][0]} -> {request.method}")
        
        if not request.user or not request.user.is_authenticated:
            print("not auth")
            return False

        if request.method in SAFE_METHODS:
            print("method safe")
            return True
        
        if int(request.user.user_level) == int(customUser.USER_LEVEL[0][0]):
            print("user level safe")
            return True
        
        print(f"return false {request.method}")
        return False