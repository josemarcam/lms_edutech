from modules.shared.serializer_field.institution import InstitutionSerializerField
from modules.user.models import CustomUser as User

class UserLevelSerializerField(InstitutionSerializerField):
    def __init__(self, slug_field=None, user_level=User.USER_LEVEL[2][0], **kwargs):
        self.user_level=user_level
        super().__init__(slug_field, **kwargs)
    
    def get_queryset(self):
        super().get_queryset()
        queryset = self.queryset
        queryset = queryset.filter(user_level=self.user_level)
        return queryset