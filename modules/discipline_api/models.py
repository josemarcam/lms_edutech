from django.db import models
from django.contrib.auth.models import User

class Discipline(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    workload = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disciplines', null=True)
    studants = models.ManyToManyField(User, null=True)
    
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
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons",null=True)
    
    def __str__(self) -> str:
        return self.name