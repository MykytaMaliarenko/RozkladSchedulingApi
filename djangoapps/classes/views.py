from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.classes.models import Class
from djangoapps.groups.models import Group
from djangoapps.classes.serializers import ClassSerializer, ClassWithoutGroupSerializer, \
    RoomsClassesSerializer, ClassWithoutRoomSerializer, ClassWithoutTeacherSerializer
from djangoapps.rooms.models import Room


class ClassViewSet(ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing all classes with all data.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassesByGroupList(generics.ListAPIView):
    """
        A list of classes by group name of group id.
    """
    serializer_class = ClassWithoutGroupSerializer

    def get_queryset(self):
        group_id: int or None = None
        group_name: str or None = None

        group_raw: str = self.kwargs["group"]
        if '-' in group_raw:
            if group_raw.index('-') != 0 and group_raw.index('-') != (len(group_raw) - 1):
                group_name = group_raw.lower()
            else:
                raise ParseError
        else:
            try:
                group_id = int(group_raw)
            except ValueError:
                raise ParseError

        if group_id is not None:
            classes = Class.objects.filter(groups__id=group_id).prefetch_related('groups', 'room', 'teacher')
            if classes:
                return classes
            else:
                raise NotFound
        else:
            try:
                group: Group = Group.objects.get(name=group_name)
                return Class.objects.filter(groups__id=group.id)
            except ObjectDoesNotExist:
                raise NotFound


class ClassesByBuildingList(generics.ListAPIView):
    """
        A list of classes by rooms in building.
    """

    serializer_class = RoomsClassesSerializer

    def get_queryset(self):
        try:
            building: int = int(self.kwargs["building"])
            return Room.objects.filter(university_building=building).prefetch_related("classes")
        except ValueError:
            raise ParseError


class ClassesByRoom(generics.ListAPIView):
    """
        A list of classes by room.
    """

    serializer_class = ClassWithoutRoomSerializer

    def get_queryset(self):
        try:
            room_id: int = int(self.kwargs["room"])
            return Class.objects.filter(room_id=room_id).prefetch_related("teacher", "groups")
        except ValueError:
            raise ParseError


class ClassesByTeacher(generics.ListAPIView):
    """
        A list of classes by teacher.
    """

    serializer_class = ClassWithoutTeacherSerializer

    def get_queryset(self):
        try:
            teacher_id: int = int(self.kwargs["teacher"])
            return Class.objects.filter(teacher_id=teacher_id).prefetch_related("room", "groups")
        except ValueError:
            raise ParseError
