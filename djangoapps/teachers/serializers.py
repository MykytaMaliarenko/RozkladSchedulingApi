from rest_framework import serializers
from djangoapps.teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """

    class Meta:
        model = Teacher
        fields = ("id", "name", "official_name",)

        read_only_fields = ("id",)
