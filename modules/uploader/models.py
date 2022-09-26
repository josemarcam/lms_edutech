from django.db import models

from modules.course.models import Lesson
 
class LessonFile(models.Model):
    
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    lessons = models.ManyToManyField(to=Lesson, related_name="files")
 
    class Meta:
        verbose_name_plural = 'Drop Boxes'