from rest_framework import serializers
from djangoapps.timeslots.models import TimeSlot


TIME_FORMAT = "%H:%M"


class TimeSlotSerializer(serializers.ModelSerializer):
    """ Serializer to represent the TimeSet model """
    time_start = serializers.TimeField(format=TIME_FORMAT)
    time_end = serializers.TimeField(format=TIME_FORMAT)

    class Meta:
        model = TimeSlot
        fields = "__all__"
