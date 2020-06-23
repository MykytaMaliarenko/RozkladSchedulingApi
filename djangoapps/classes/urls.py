from rest_framework import routers

from djangoapps.classes.views import ClassViewSet

router = routers.DefaultRouter()
router.register(r'classes', ClassViewSet, basename='classes')

urlpatterns = router.urls
