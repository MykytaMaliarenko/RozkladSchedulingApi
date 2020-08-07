from rest_framework import routers
from django.conf.urls import url, include

from djangoapps.rooms.views import RoomsViewSet, BuildingsViewSet, \
    RoomsInBuildingList, EmptyRoomsInBuildingList

buildings_list = BuildingsViewSet.as_view({
    "get": "list",
})

router = routers.DefaultRouter()
router.register(r'rooms', RoomsViewSet, basename='rooms')

urlpatterns = [
    url(r'rooms/buildings', buildings_list, name="rooms-buildings"),

    url(r'^rooms/building/(?P<building>\d+)$',
        RoomsInBuildingList.as_view(), name="rooms-in-building"),

    url(r'^rooms/free/building/(?P<building>\d+)$',
        EmptyRoomsInBuildingList.as_view(), name="empty-rooms-in-building"),

    url(r'', include(router.urls)),
]
