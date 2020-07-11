from rest_framework import routers, permissions
from django.contrib import admin
from django.conf.urls import url, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Rozkald Scheduling API",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mykytamaliarenko@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    url(r'^api/v1/', include('djangoapps.classes.urls')),
    url(r'^api/v1/', include('djangoapps.groups.urls')),
    url(r'^api/v1/', include('djangoapps.teachers.urls')),
    url(r'^api/v1/', include('djangoapps.rooms.urls')),
    url(r'^api/v1/', include('djangoapps.timeslots.urls')),
]
