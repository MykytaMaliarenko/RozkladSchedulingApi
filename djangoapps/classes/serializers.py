from rest_framework import serializers
from djangoapps.classes.models import Class
from djangoapps.groups.serializers import GroupSerializer
from djangoapps.rooms.serializers import RoomSerializer
from djangoapps.teachers.serializers import TeacherSerializer
from djangoapps.timeslots.serializers import TimeSlotSerializer


class ClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Class model """
    teacher = TeacherSerializer()
    room = RoomSerializer()
    group = GroupSerializer()
    time_slot = TimeSlotSerializer()

    class Meta:
        model = Class
        fields = "__all__"
