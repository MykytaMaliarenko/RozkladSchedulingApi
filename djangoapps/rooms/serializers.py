from rest_framework import serializers
from djangoapps.rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Room model """

    class Meta:
        model = Room
        fields = ("id", "name", "university_building",)

        read_only_fields = ("id",)


class RoomBuildingOnlySerializer(serializers.ModelSerializer):
    """ Serializer to represent a building value from Room model """

    class Meta:
        model = Room
        fields = ("university_building",)

    def to_representation(self, instance: Room):
        return instance['university_building']
