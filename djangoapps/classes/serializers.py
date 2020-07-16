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
    group = GroupSerializer()

    class Meta:
        model = Class
        fields = "__all__"


class ClassWithoutGroupSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model without Room """
    teacher = TeacherSerializer()
    room = RoomSerializer()

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "teacher",
                  "room", "time_slot")


class RawClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent raw Class model without teacher, room, group """

    class Meta:
        model = Class
        fields = ("id", "name", "type", "day_of_week", "week_number", "time_slot")


class RoomsClassesSerializer(serializers.ModelSerializer):
    """ Serializer to represent Room model and classes that take place in it """

    classes = RawClassSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "name", "classes")
