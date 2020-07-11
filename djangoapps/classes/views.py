from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.exceptions import APIException, NotFound, ParseError
from rest_framework.viewsets import ReadOnlyModelViewSet

from djangoapps.classes.models import Class
from djangoapps.groups.models import Group
from djangoapps.classes.serializers import ClassSerializer, ClassWithoutGroupSerializer


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
            classes = Class.objects.filter(group_id=group_id)
            if classes:
                return classes
            else:
                raise NotFound
        else:
            try:
                group: Group = Group.objects.get(name=group_name)
                return Class.objects.filter(group_id=group.id)
            except ObjectDoesNotExist:
                raise NotFound
