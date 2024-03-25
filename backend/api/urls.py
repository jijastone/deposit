from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AreaViewSet,)

app_name = 'api'

router = DefaultRouter()

router.register('area', AreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
