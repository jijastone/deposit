from drf_extra_fields.fields import Base64ImageField
from deposits.models import (License, Area, Сoordinates, OPI, Owner, Deposit)
from rest_framework.fields import (ReadOnlyField,
                                   SerializerMethodField)
from rest_framework.relations import PrimaryKeyRelatedField
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

class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class LicenseSerializer(ModelSerializer):
    name = ReadOnlyField(source='owner.name')
    address = ReadOnlyField(source='owner.address')

    class Meta:
        model = License
        fields = ('address', 'name', 'registration', 'end_date')


class ReadAreaSerializer(ModelSerializer):
    owners = LicenseSerializer(
        many=True, source='arealicense')
    coordinates = СoordinatesSerializer(many=True)
    opi = OPISerializer(many=True)
    deposit = DepositSerializer()
    class Meta:
        model = Area
        fields = (
            'owners',
            'deposit',
            'coordinates',
            'name',
            'opi',
            'category_a',
            'category_b',
            'category_c1',
            'category_c2',
            'year_estimation',
        )
class CreateOwnerSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Owner.objects.all(),
                                source='owner.id')

    class Meta:
        model = License
        fields = ('id', 'number', 'registration', 'end_date')
class WriteAreaSerializer(ModelSerializer):
    coordinates = СoordinatesSerializer(many=True)
    owners = CreateOwnerSerializer(many=True)
    opi = PrimaryKeyRelatedField(
        queryset=OPI.objects.all(),
        many=True,
    )
    deposit = PrimaryKeyRelatedField(
        queryset=Deposit.objects.all(),
        source='deposit.id'
    )
    class Meta:
        model = Area
        fields = (
            'owners',
            'deposit',
            'coordinates',
            'name',
            'opi',
            'category_a',
            'category_b',
            'category_c1',
            'category_c2',
            'year_estimation'
        )

    def create(self, validated_data):
        coordinates = validated_data.pop('coordinates')
        opi = validated_data.pop('opi')
        owners = validated_data.pop('owners')
        deposit = validated_data.pop('deposit')
        area = Area.objects.create(**validated_data, deposit=deposit['id'])
        area.opi.set(opi)
        License.objects.bulk_create(
            [License(
                owner=owner['owner']['id'],
                area=area,
                number=owner['number'],
                registration=owner['registration'],
                end_date=owner['end_date']
            ) for owner in owners]
        )
        res_c =[]
        for coordinat in coordinates:
            coordinat = Сoordinates.objects.create(
                long=coordinat['long'],
                lat=coordinat['lat']
            )
            res_c.append(coordinat)
        area.coordinates.set(res_c)
        return area

