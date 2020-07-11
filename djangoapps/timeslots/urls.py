from rest_framework import routers

from djangoapps.timeslots.views import TimeSlotsViewSet

router = routers.DefaultRouter()
router.register(r'timeslots', TimeSlotsViewSet, basename='timeslots')

urlpatterns = router.urls
