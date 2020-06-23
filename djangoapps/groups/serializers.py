from rest_framework import serializers
from djangoapps.groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group model """

    class Meta:
        model = Group
        fields = ("id", "name")

        read_only_fields = ("id",)
