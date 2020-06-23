from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.groups.models import Group
from djangoapps.groups.serializers import GroupSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing groups.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
