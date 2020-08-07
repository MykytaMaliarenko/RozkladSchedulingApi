from django.db.models import Q
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.teachers.models import Teacher
from djangoapps.teachers.serializers import TeacherSerializer


class TeachersViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all teachers.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeachersSearchByNameList(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        query: str = self.kwargs["query"]
        return Teacher.objects.filter(Q(name__icontains=query) |
                                      Q(official_name__icontains=query))[:10]
