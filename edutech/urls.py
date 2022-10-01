from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers

from modules.course.views import (
    DisciplineViews,
    ModuleViews,
    LessonViews,
    CourseViews
)
from modules.exam.views import ExamViews, ExerciseViews

from modules.uploader.views import LessonFileViewset
from modules.user.views import CourseClassViews, InstitutionViews, UserViews


router = routers.DefaultRouter()

router.register(r'courses', CourseViews, basename="courses")
router.register(r'disciplines', DisciplineViews, basename="disciplines")
router.register(r'modules', ModuleViews, basename="modules")
router.register(r'lessons', LessonViews, basename="lessons")
router.register(r'lesson_files', LessonFileViewset, basename="lesson_files")

router.register(r'users', UserViews, basename="users")
router.register(r'institutions', InstitutionViews, basename="institutions")
router.register(r'course-classes', CourseClassViews, basename="course-classes")

router.register(r'exams', ExamViews, basename="exams")
router.register(r'exercises', ExerciseViews, basename="exercises")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('disciplines/', include('modules.course.views'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)