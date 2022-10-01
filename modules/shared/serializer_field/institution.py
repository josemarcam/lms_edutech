from rest_framework.serializers import SlugRelatedField


class InstitutionSerializerField(SlugRelatedField):
    def __init__(self, slug_field=None, object_attr="institution", **kwargs):
        self.object_attr = object_attr
        super().__init__(slug_field, **kwargs)
    
    def get_queryset(self):
        queryset = self.queryset
        object_attr = self.object_attr
        request = self.context.get('request', None)
        queryset = queryset.filter(**{object_attr: request.user.institution})
        self.queryset = queryset
        return queryset