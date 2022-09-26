from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    ChoiceField,
    SlugRelatedField
)
from modules.user.models import CustomUser as User, Institution

class UserSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    first_name = CharField(required=True, allow_blank=False, max_length=100)
    last_name = CharField(required=True, allow_blank=False, max_length=100)
    username = CharField(required=True, allow_blank=False, max_length=100)
    email = CharField(required=True, allow_blank=False, max_length=100)
    password = CharField(required=True, allow_blank=False, max_length=100)
    user_level = ChoiceField(choices=User.USER_LEVEL)
    institution = SlugRelatedField(slug_field="id", read_only=True, many=False)


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

class InstitutionSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    users = SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True, many=True)
    


    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        instance : Institution = Institution.objects.create_user(**validated_data)
        return instance

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.workload = validated_data.get('workload', instance.workload)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.professor = validated_data.get('professor', instance.professor)
    #     instance.save()
    #     return instance