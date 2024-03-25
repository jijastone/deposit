from drf_extra_fields.fields import Base64ImageField
from deposits.models import (License, Area, Сoordinates, OPI)
from rest_framework.fields import (ReadOnlyField,
                                   SerializerMethodField)
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, ValidationError


class OPISerializer(ModelSerializer):
    class Meta:
        model = OPI
        fields = '__all__'


class СoordinatesSerializer(ModelSerializer):
    class Meta:
        model = Сoordinates
        fields = '__all__'


class LicenseSerializer(ModelSerializer):
    name = ReadOnlyField(source='owner.name')
    address = ReadOnlyField(source='owner.address')

    class Meta:
        model = License
        fields = ('address', 'name', 'registration', 'end_date')


class AreaSerializer(ModelSerializer):
    owners = LicenseSerializer(
        many=True, source='arealicense')
    coordinates = СoordinatesSerializer(many=True)
    opi = OPISerializer(many=True)

    class Meta:
        model = Area
        fields = (
            'owners',
            'coordinates',
            'name',
            'opi',
            'category_a',
            'category_b',
            'category_c1',
            'category_c2'
        )


