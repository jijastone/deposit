from django_filters.rest_framework import FilterSet, filters

from deposits.models import Area


class AreaFilter(FilterSet):
    is_not_license = filters.BooleanFilter(field_name='arealicense', lookup_expr='isnull')
    opi = filters.CharFilter(
        method='get_opi')
    deposit_name = filters.CharFilter(
        method='get_deposit_name')
    okato_name = filters.CharFilter(
        method='get_okato_name')

    def get_opi(self, areas, name, value):
        if value:
            return areas.filter(opi__name__icontains=value.lower())
        return areas

    def get_deposit_name(self, areas, name, value):
        if value:
            return areas.filter(deposit__name__icontains=value.lower())
        return areas

    def get_okato_name(self, areas, name, value):
        if value:
            return areas.filter(deposit__okato__name__icontains=value.lower())
        return areas

    class Meta:
        model = Area
        fields = ('name', 'is_not_license')
