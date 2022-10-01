from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    JSONField
)
from modules.exam.models import Exam, Exercise
from modules.user.models import CourseClass
from modules.shared.serializer_field.institution import InstitutionSerializerField

class ExamSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    course_class = InstitutionSerializerField(slug_field="id", read_only=False, queryset=CourseClass.objects.all())
    exam_id = InstitutionSerializerField(slug_field="id", read_only=False, allow_null=True, queryset=Exam.objects.all())
    exercises = InstitutionSerializerField(many=True, slug_field="id", read_only=False, queryset=Exercise.objects.all(), object_attr="exam__institution")


    def create(self, validated_data):
        """
        Create and return a new `Exam` instance, given the validated data.
        """
        exercises = validated_data.get("exercises")

        del validated_data["exercises"]
        
        instance : Exam = Exam.objects.create(**validated_data)
        instance.exercises.set(exercises)

        return instance

    def update(self, instance, validated_data):
        instance.exam_id = validated_data.get('exam_id', instance.exam_id)
        instance.course_class = validated_data.get('course_class', instance.course_class)
        instance.exercises.set(validated_data.get('exercises', instance.exercises))
        
        instance.save()
        return instance

class ExerciseSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    statement = CharField(required=True, allow_blank=False, max_length=100)
    answer = CharField(required=True, allow_blank=False, max_length=100)
    alternatives = JSONField(required=True)
    exam = InstitutionSerializerField(slug_field="id", read_only=False, queryset=Exam.objects.all())


    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        instance : Exercise = Exercise.objects.create(**validated_data)
        return instance

class AssignExamSerializer(Serializer):
    
    id = IntegerField(read_only=True)
    statement = CharField(required=True, allow_blank=False, max_length=100)
    answer = CharField(required=True, allow_blank=False, max_length=100)
    alternatives = JSONField(required=True)
    exam = InstitutionSerializerField(slug_field="id", read_only=False, queryset=Exam.objects.all())


    def create(self, validated_data):
        """
        Create and return a new `Discipline` instance, given the validated data.
        """
        instance : Exercise = Exercise.objects.create(**validated_data)
        return instance