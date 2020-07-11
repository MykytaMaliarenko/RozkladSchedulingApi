from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.groups.models import Group
from djangoapps.groups.serializers import GroupSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing groups.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupSearchByNameList(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        request: str = self.kwargs["searchRequest"]
        return Group.objects.filter(name__contains=request.lower())
