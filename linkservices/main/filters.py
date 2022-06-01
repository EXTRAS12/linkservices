import django_filters
from django import forms

from site_app.models import WebSite

from site_app.models import Category


class SiteFilter(django_filters.FilterSet):
    """Фильтр для каталога"""
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    yandex_x__gt = django_filters.NumberFilter(field_name='yandex_x', lookup_expr='gt')
    yandex_x__lt = django_filters.NumberFilter(field_name='yandex_x', lookup_expr='lt')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = WebSite
        fields = ['category']
