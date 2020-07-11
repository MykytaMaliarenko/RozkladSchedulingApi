from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.teachers.models import Teacher
from djangoapps.teachers.serializers import TeacherSerializer


class TeachersViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all teachers.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
