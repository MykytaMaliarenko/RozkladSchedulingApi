from rest_framework import routers

from djangoapps.teachers.views import TeachersViewSet

router = routers.DefaultRouter()
router.register(r'teachers', TeachersViewSet, basename='teachers')

urlpatterns = router.urls
