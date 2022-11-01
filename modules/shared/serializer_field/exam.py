from modules.shared.serializer_field.institution import InstitutionSerializerField
from modules.user.models import CustomUser as User


class AssingUserSerializerField(InstitutionSerializerField):
    def __init__(self, slug_field=None, **kwargs):
        super().__init__(slug_field, **kwargs)
    
    def get_queryset(self):
        super().get_queryset()
        queryset = self.queryset
        request = self.context.get('request', None)
        current_user = request.user
        queryset = queryset.filter(user=current_user)
        return queryset