from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(10 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
