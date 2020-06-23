from rest_framework import serializers
from djangoapps.timeslots.models import TimeSlot


class TimeSlotSerializer(serializers.ModelSerializer):
    """ Serializer to represent the TimeSet model """

    class Meta:
        model = TimeSlot
        fields = "__all__"
