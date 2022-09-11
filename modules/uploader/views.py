from rest_framework import viewsets, parsers
from modules.uploader.models import LessonFile
from modules.uploader.serializers import LessonFileSerializer


class LessonFileViewset(viewsets.ModelViewSet):
 
    queryset = LessonFile.objects.all()
    serializer_class = LessonFileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']