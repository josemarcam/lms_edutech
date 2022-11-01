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
    
    def is_main(self) -> bool:
        return not bool(self.exam_id)

class Exercise(models.Model):

    statement = models.CharField(max_length=255, blank=False, null=False)
    answer = models.IntegerField(blank=False, null=False)
    alternatives = models.JSONField()

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exercises", null=False)

class AssignExam(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    score = models.IntegerField(null=True)
    
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="assignments", null=False)
    source_exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="source_assignments", null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments", null=False)
    #TODO: fazer final_score e final_percent

    def get_final_score(self) -> int:
        
        exam_exercises = self.exam.exercises.all()
        right_aswers = 0
        total_aswers = len(exam_exercises)
        studant_assign_aswers = AssignAswer.objects.filter(assign=self.id)
        
        for exercise in exam_exercises:
            
            studant_aswer = studant_assign_aswers.filter(exercise=exercise).first()
            if exercise.answer == studant_aswer.answer:
                right_aswers += 1

        final_score = (right_aswers/total_aswers) * 100

        return final_score
    
    def finalize(self) -> bool:

        score = self.get_final_score()
        self.score = score
        self.done = True
        self.save()
        return True

        


class AssignAswer(models.Model):

    assign = models.ForeignKey(AssignExam, on_delete=models.CASCADE, related_name="answers", null=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="assing_answers", null=False)
    answer = models.IntegerField(blank=False, null=False)