from django.db import models
from modules.user.models import CourseClass, Institution, CustomUser as User
from random import randint
from django.db.models import Q


class Exam(models.Model):
    
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name="exams", null=True)
    exam_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=False)

    def get_random_child(self):
        children = Exam.objects.filter(Q(exam_id = self.id) | Q(id = self.id)).all()
        count_exams = len(children)
        exam_index = randint(0, count_exams -1)
        return children[exam_index]

class Exercise(models.Model):

    statement = models.CharField(max_length=255, blank=False, null=False)
    answer = models.IntegerField(blank=False, null=False)
    alternatives = models.JSONField()

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exercises", null=False)

class AssignExam(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="assignments", null=False)
    source_exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="source_assignments", null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments", null=False)

class AssignAswer(models.Model):

    assign = models.ForeignKey(AssignExam, on_delete=models.CASCADE, related_name="answers", null=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="assing_answers", null=False)
    answer = models.IntegerField(blank=False, null=False)