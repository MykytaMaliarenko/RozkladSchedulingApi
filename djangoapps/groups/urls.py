from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from djangoapps.groups.views import GroupViewSet, GroupSearchByNameList

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    url(r'^groups/search/(?P<searchRequest>.+)$',
        GroupSearchByNameList.as_view(), name="groups-search"),

    url(r'', include(router.urls)),
]
