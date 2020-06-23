from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.rooms.models import Room
from djangoapps.rooms.serializers import RoomSerializer


class RoomsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all rooms.
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
