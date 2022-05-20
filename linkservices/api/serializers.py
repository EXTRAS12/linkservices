from rest_framework import serializers
from site_app.models import WebSite, Category
from link_app.models import Link


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class WebSiteSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка сайтов"""
    category = CategorySerializer()

    class Meta:
        model = WebSite
        fields = ('id', 'url', 'category', 'update', 'created')


class LinkSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка ссылок"""
    url = WebSiteSerializer(read_only=True)

    class Meta:
        model = Link
        fields = ('id', 'link', 'valid_date', 'count_month', 'price_per_item', 'total_price', 'url',
                  'created', 'update')
