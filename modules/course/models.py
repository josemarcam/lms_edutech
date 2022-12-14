from django.db import models
from modules.user.models import CustomUser as User, Institution

class Discipline(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    workload = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="disciplines", null=True)

    
    def __str__(self) -> str:
        return self.name

class Module(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)

    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="modules",null=True)


    def __str__(self) -> str:
        return self.name

class Lesson(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")

    
    def __str__(self) -> str:
        return self.name

class Course(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="courses", null=True)
    disciplines = models.ManyToManyField(Discipline, related_name="courses")
    studants = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name