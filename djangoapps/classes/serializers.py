from rest_framework import serializers
from djangoapps.classes.models import Class
from djangoapps.groups.serializers import GroupSerializer
from djangoapps.rooms.models import Room
from djangoapps.rooms.serializers import RoomSerializer
from djangoapps.teachers.serializers import TeacherSerializer


class ClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model """
    teacher = TeacherSerializer()
    room = RoomSerializer()
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = "__all__"


class ClassWithoutGroupSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model without Group """
    teacher = TeacherSerializer()
    room = RoomSerializer()

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "teacher",
                  "room", "time_slot")


class ClassWithoutRoomSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model without Room """
    teacher = TeacherSerializer()
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "teacher",
                  "groups", "time_slot")


class ClassWithoutTeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model without Teacher """
    room = RoomSerializer()
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "room",
                  "groups", "time_slot")


class RawClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent raw Class model without teacher, room, group """

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "time_slot")
