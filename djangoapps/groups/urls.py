from rest_framework import routers

from djangoapps.groups.views import GroupViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = router.urls
