from deposits.models import Area
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (AreaSerializer)
from .fillters import RecipeFilter


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter
