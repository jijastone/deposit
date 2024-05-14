from deposits.models import Area, OPI
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ( ReadAreaSerializer, WriteAreaSerializer, OPISerializer)
from .fillters import AreaFilter


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AreaFilter

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadAreaSerializer
        return WriteAreaSerializer


class OpiViewSet(ModelViewSet):
    queryset = OPI.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OPISerializer
