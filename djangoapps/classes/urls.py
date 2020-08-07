from rest_framework import routers
from django.conf.urls import url, include

from djangoapps.classes.views import ClassViewSet, ClassesByGroupList, \
    ClassesByRoom, ClassesByTeacher

router = routers.DefaultRouter()
router.register(r'classes', ClassViewSet, basename='classes')

urlpatterns = [
    url(r'^classes/group/(?P<group>.+)/$',
        ClassesByGroupList.as_view(), name="classes-by-group"),

    url(r'^classes/room/(?P<room>\d+)/$',
        ClassesByRoom.as_view(), name="classes-by-room"),

    url(r'^classes/teacher/(?P<teacher>\d+)/$',
        ClassesByTeacher.as_view(), name="classes-by-teacher"),

    url(r'', include(router.urls)),
]
