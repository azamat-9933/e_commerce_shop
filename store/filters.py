import django_filters
from store.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    characteristic = django_filters.CharFilter(method='filter_by_characteristic')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'characteristic']

    def filter_by_characteristic(self, queryset, name, value):
        return queryset.filter(characteristics__value__icontains=value).distinct()
