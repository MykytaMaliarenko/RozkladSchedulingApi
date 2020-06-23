from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.timeslots.models import TimeSlot
from djangoapps.timeslots.serializers import TimeSlotSerializer


class TimeSlotsViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all time slots.
    """

    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
