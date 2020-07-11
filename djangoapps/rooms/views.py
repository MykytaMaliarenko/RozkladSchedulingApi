from rest_framework import status, generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.rooms.models import Room
from djangoapps.rooms.serializers import RoomSerializer, RoomBuildingOnlySerializer


class RoomsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all rooms.
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomsBuildingsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing of all buildings.
    """

    queryset = Room.objects.distinct('university_building')
    serializer_class = RoomBuildingOnlySerializer
