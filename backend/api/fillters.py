from django_filters.rest_framework import FilterSet, filters

from deposits.models import Area


class RecipeFilter(FilterSet):
    is_not_license = filters.BooleanFilter(field_name='arealicense', lookup_expr='isnull')
    opi = filters.CharFilter(
        method='get_opi')

    def get_opi(self, areas, name, value):
        if value:
            return areas.filter(opi__name__icontains=value.lower())
        return areas

    class Meta:
        model = Area
        fields = ('name','is_not_license')