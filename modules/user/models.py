from django.db import models
from django.contrib.auth.models import AbstractUser


class Institution(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #TODO: add more field to institution registration

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    
    USER_LEVEL = (
        (1,"administrator"), 
        (2,"professor"), 
        (3,"studant")
    )
    user_level = models.CharField(max_length=9,
                  choices=USER_LEVEL,
                  default=1)
    
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="users")

    # REQUIRED_FIELDS = ['institution']

class CourseClass(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=False)
    studants = models.ManyToManyField(CustomUser, related_name="course_class")

    def user_is_in_class(self, user_id):
        studant = self.studants.filter(id=user_id).first()
        return bool(studant)

    def __str__(self):
        return self.name