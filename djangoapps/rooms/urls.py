from rest_framework import routers
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from djangoapps.rooms.views import RoomsViewSet, BuildingsViewSet, \
    RoomsInBuildingList

buildings_list = BuildingsViewSet.as_view({
    "get": "list",
})

router = routers.DefaultRouter()
router.register(r'rooms', RoomsViewSet, basename='rooms')

urlpatterns = [
    url(r'rooms/buildings', buildings_list, name="rooms-buildings"),

    url(r'^rooms/building/(?P<building>\d+)$',
        RoomsInBuildingList.as_view(), name="rooms-in-building"),

    url(r'', include(router.urls)),
]
