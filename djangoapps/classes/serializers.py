from rest_framework import serializers
from djangoapps.classes.models import Class
from djangoapps.groups.serializers import GroupSerializer
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
