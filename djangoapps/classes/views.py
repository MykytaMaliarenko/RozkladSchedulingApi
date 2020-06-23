from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.classes.models import Class
from djangoapps.classes.serializers import ClassSerializer


class ClassViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all classes with all data.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
