from rest_framework import serializers
from djangoapps.rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Room model """

    class Meta:
        model = Room
        fields = ("id", "name", "university_building",)

        read_only_fields = ("id",)
