from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from modules.exam.models import AssignAswer, AssignExam, Exam, Exercise
from modules.user.models import CustomUser as User
from modules.exam.serializers import AssignAswerSerializer, AssignExamSerializer, ExamSerializer, ExerciseSerializer
from modules.shared.permissions.custom_permission import AtLeastProfessorOrClassCoursePermission, AtLeastProfessorPermission
from http import HTTPStatus


class ExamViews(ModelViewSet):
    """
    List all courses, or create a new discipline.
    """
    serializer_class = ExamSerializer
    permission_classes = [AtLeastProfessorOrClassCoursePermission]

    @action(detail=True, methods=['GET'], name='Assign Studant to exam', serializer_class=AssignExamSerializer, permission_classes=[])
    def assign(self,request, pk=None):
        
        exam : Exam = self.get_object()
        user = request.user
        user_exam = exam.get_random_child()
        source_exam = user_exam if user_exam.exam_id == None else user_exam.exam_id

        if len(user_exam.exercises.all()) <= 0:
            return Response(status=HTTPStatus.NOT_FOUND)
        
        assignment = AssignExam.objects.filter(user=user, source_exam=source_exam).first()
        if not assignment:
            assignment = AssignExam.objects.create(exam=user_exam, user=user, source_exam=source_exam)
            # TODO: think of some other stuff to do in this case
        
        exercises = assignment.exam.exercises.all()
        exercise_serializers = []
        for exercise in exercises:
            exercise_serializers.append(ExerciseSerializer(exercise).data)
        return Response(self.get_serializer(assignment).data)
        
    @action(detail=True, methods=['POST','GET'], name='Assign Aswer to exam', serializer_class=AssignAswerSerializer)
    def assign_aswer(self,request, pk=None):
        
        exam : Exam = self.get_object()
        if not exam.is_main():
            return Response(status=HTTPStatus.NOT_FOUND)

        user = request.user
        assignment = AssignExam.objects.filter(user=user, source_exam=exam).first()
        if not assignment or assignment.done:
            return Response(status=HTTPStatus.NOT_FOUND)
        
        if request.method == "GET":
            assign_aswers = AssignAswer.objects.filter(assign=assignment).all()
            serializerd_aswers = []
            for aswer in assign_aswers:
                serializerd_aswers.append(AssignAswerSerializer(aswer).data)

            return Response(serializerd_aswers, HTTPStatus.OK)
        
        serializer : AssignAswerSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("OK", HTTPStatus.CREATED)
        
    @action(detail=True, methods=['GET'], name='Finish assign and get final score', serializer_class=AssignExamSerializer, permission_classes=[])
    def assign_finalize(self,request, pk=None):
        
        exam : Exam = self.get_object()
        if not exam.is_main():
            return Response(status=HTTPStatus.NOT_FOUND)

        user = request.user
        assignment = AssignExam.objects.filter(user=user, source_exam=exam).first()
        if not assignment:
            return Response(status=HTTPStatus.NOT_FOUND)

        if not assignment.done:
            assignment.finalize()

        return Response(self.get_serializer(assignment).data, HTTPStatus.OK)
    
    @action(detail=True, methods=['GET'], name='Get all aswers for exam', serializer_class=ExamSerializer, permission_classes=[AtLeastProfessorPermission])
    def get_exam_aswers(self,request, pk=None):
        
        exam : Exam = self.get_object()
        if not exam.is_main():
            return Response(status=HTTPStatus.NOT_FOUND)
        
        exam_assigns = exam.assignments.all()
        exam_asnwers = [AssignExamSerializer(assign).data for assign in exam_assigns]

        return Response(exam_asnwers, HTTPStatus.OK)
        
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
    permission_classes = [AtLeastProfessorOrClassCoursePermission]

    def get_queryset(self):
        return Exercise.objects.filter(exam__institution = self.request.user.institution.id)

    def perform_create(self, serializer):
        serializer.save()
    