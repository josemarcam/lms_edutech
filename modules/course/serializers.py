from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    SlugRelatedField
)
from modules.user.models import CustomUser as User

from modules.course.models import (
    Course,
    Discipline,
    Module,
    Lesson
)

class DisciplineSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    workload = IntegerField(required=True)
    description = CharField(required=False, allow_blank=True, max_length=255)
    professor = SlugRelatedField(many=False, slug_field=User.USERNAME_FIELD, read_only=False, queryset=User.objects.all(), allow_null=True)
    courses = SlugRelatedField(many=True, slug_field="id", read_only=True)

    modules = SlugRelatedField(many=True, slug_field="name", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        instance : Discipline = Discipline.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.workload = validated_data.get('workload', instance.workload)
        instance.description = validated_data.get('description', instance.description)
        instance.professor = validated_data.get('professor', instance.professor)
        instance.save()
        return instance

class ModuleSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    description = CharField(required=False, allow_blank=True, max_length=255)

    discipline = SlugRelatedField(many=False, slug_field="id", read_only=False, queryset=Discipline.objects.all(), allow_null=True)
    lessons = SlugRelatedField(many=True, slug_field="id", read_only=True)


    def create(self, validated_data):
        """
        Create and return a new `Module` instance, given the validated data.
        """
           
        instance : Module = Module.objects.create(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.discipline = validated_data.get('discipline', instance.discipline)
        instance.save()
        return instance

class LessonSerializer(Serializer):

    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    description = CharField(required=False, allow_blank=True, max_length=255)

    module = SlugRelatedField(many=False, slug_field="id", read_only=False, queryset=Module.objects.all(), allow_null=True)
    files = SlugRelatedField(many=True, slug_field="document", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Lesson` instance, given the validated data.
        """
            
        instance : Lesson = Lesson.objects.create(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.module = validated_data.get('module', instance.module)
        instance.save()
        return instance

class CourseSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    name = CharField(required=True, allow_blank=False, max_length=100)
    description = CharField(required=False, allow_blank=True, max_length=255)
    studants = SlugRelatedField(many=True, slug_field=User.USERNAME_FIELD, read_only=False, queryset=User.objects.all())
    disciplines = SlugRelatedField(many=True, slug_field="id", read_only=False, queryset=Discipline.objects.all())

    # modules = SlugRelatedField(many=True, slug_field="name", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        studants = validated_data.get("studants")
        disciplines = validated_data.get("disciplines")
        
        del validated_data['studants']
        del validated_data['disciplines']
        
        instance : Course = Course.objects.create(**validated_data)
        instance.studants.set(studants)
        instance.disciplines.set(disciplines)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.studants.set(validated_data.get('studants', instance.studants))
        instance.disciplines.set(validated_data.get('disciplines', instance.disciplines))
        instance.save()
        return instance