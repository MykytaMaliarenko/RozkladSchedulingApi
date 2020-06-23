from rest_framework import routers

from djangoapps.rooms.views import RoomsViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomsViewSet, basename='rooms')

urlpatterns = router.urls
