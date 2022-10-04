from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from modules.exam.models import AssignExam, Exam, Exercise
from modules.user.models import CustomUser as User
from modules.exam.serializers import ExamSerializer, ExerciseSerializer
from modules.shared.permissions.custom_permission import AtLeastProfessorPermission


class ExamViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    # queryset = Course.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [AtLeastProfessorPermission]

    @action(detail=True, methods=['GET'], name='Assign Studant to exam', serializer_class=ExamSerializer)
    def assign(self,request, pk=None):
        
        exam : Exam = self.get_object()
        user = request.user
        user_exam = exam.get_random_child()
        source_exam = user_exam if user_exam.exam_id == None else user_exam.exam_id
        
        assignment = AssignExam.objects.filter(user=user, source_exam=source_exam)
        if not assignment:
            assignment = AssignExam.objects.create(exam=user_exam, user=user, source_exam=source_exam)
            # TODO: think of some other stuff to do in this case
        
        serializer = self.serializer_class(user_exam)
        return Response(serializer.data)        

    def get_queryset(self):
        
        user : User = self.request.user
        if int(user.user_level) == User.USER_LEVEL[2][0]:
            user_course_class = user.course_class
            
            classes_id = []
            for course_class in user_course_class.all():
                classes_id.append(course_class.id)
            
            return Exam.objects.filter(institution = self.request.user.institution.id, course_class__in=classes_id)
        
        return Exam.objects.filter(institution = self.request.user.institution.id)

    def perform_create(self, serializer):
        serializer.save(institution=self.request.user.institution)

    
    

class ExerciseViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    # queryset = Course.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [AtLeastProfessorPermission]

    def get_queryset(self):
        return Exercise.objects.filter(exam__institution = self.request.user.institution.id)

    def perform_create(self, serializer):
        serializer.save()
    