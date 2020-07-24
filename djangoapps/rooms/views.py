from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.rooms.models import Room
from djangoapps.rooms.serializers import RoomSerializer, RoomBuildingOnlySerializer


class RoomsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all rooms.
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BuildingsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing of all buildings.
    """

    queryset = Room.objects.values('university_building').distinct().all()
    serializer_class = RoomBuildingOnlySerializer

    @method_decorator(cache_page(10 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RoomsInBuildingList(generics.ListAPIView):
    """
        A list of all room in building.
    """

    serializer_class = RoomSerializer

    def get_queryset(self):
        try:
            building = int(self.kwargs['building'])
            return Room.objects.filter(university_building=building)
        except ValueError:
            raise ParseError
