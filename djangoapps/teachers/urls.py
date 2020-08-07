from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from djangoapps.teachers.views import TeachersViewSet, TeachersSearchByNameList

router = routers.DefaultRouter()
router.register(r'teachers', TeachersViewSet, basename='teachers')

urlpatterns = [
    url(r'^teachers/search/(?P<query>.+)$',
        TeachersSearchByNameList.as_view(), name="groups-search"),

    url(r'', include(router.urls)),
]
