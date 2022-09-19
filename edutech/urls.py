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

from modules.uploader.views import LessonFileViewset


router = routers.DefaultRouter()
router.register(r'courses', CourseViews, basename="courses")
router.register(r'disciplines', DisciplineViews, basename="disciplines")
router.register(r'modules', ModuleViews, basename="modules")
router.register(r'lessons', LessonViews, basename="lessons")
router.register(r'lesson_files', LessonFileViewset, basename="lesson_files")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('disciplines/', include('modules.course.views'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)