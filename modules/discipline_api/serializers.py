from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    SlugRelatedField
)
from django.contrib.auth.models import User


from modules.discipline_api.models import (
    Discipline,
    Module,
    Lesson
)

class DisciplineSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    workload = IntegerField(required=True)
    description = CharField(required=False, allow_blank=True, max_length=255)
    professor = SlugRelatedField(many=False, slug_field=User.USERNAME_FIELD, read_only=False, queryset=User.objects.all())
    studants = SlugRelatedField(many=True, slug_field=User.USERNAME_FIELD, read_only=False, queryset=User.objects.all())

    modules = SlugRelatedField(many=True, slug_field="name", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        print(validated_data)
        studants = validated_data.get("studants")
        
        del validated_data['owner']
        del validated_data['studants']
        
        instance : Discipline = Discipline.objects.create(**validated_data)
        instance.studants.set(studants)
        return instance

class ModuleSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    description = CharField(required=False, allow_blank=True, max_length=255)

    discipline = SlugRelatedField(many=False, slug_field="name", read_only=False, queryset=Discipline.objects.all())
    lessons = SlugRelatedField(many=True, slug_field="name", read_only=True)


    def create(self, validated_data):
        """
        Create and return a new `Module` instance, given the validated data.
        """
        
        del validated_data['owner']
        
        instance : Module = Module.objects.create(**validated_data)
        return instance

class LessonSerializer(Serializer):

    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    description = CharField(required=False, allow_blank=True, max_length=255)

    module = SlugRelatedField(many=False, slug_field="name", read_only=False, queryset=Module.objects.all())
    files = SlugRelatedField(many=True, slug_field="document", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Lesson` instance, given the validated data.
        """
        
        del validated_data['owner']
        
        instance : Lesson = Lesson.objects.create(**validated_data)
        return instance
