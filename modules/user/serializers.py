from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    ChoiceField,
)
from modules.user.models import customUser as User

class UserSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    first_name = CharField(required=True, allow_blank=False, max_length=100)
    last_name = CharField(required=True, allow_blank=False, max_length=100)
    username = CharField(required=True, allow_blank=False, max_length=100)
    email = CharField(required=True, allow_blank=False, max_length=100)
    password = CharField(required=True, allow_blank=False, max_length=100)
    user_level = ChoiceField(choices=User.USER_LEVEL)


    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        instance : User = User.objects.create_user(**validated_data)
        return instance

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.workload = validated_data.get('workload', instance.workload)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.professor = validated_data.get('professor', instance.professor)
    #     instance.save()
    #     return instance