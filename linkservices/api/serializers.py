from rest_framework import serializers
from site_app.models import WebSite
from link_app.models import Link


class WebSiteSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка сайтов"""
    class Meta:
        model = WebSite
        fields = ('id', 'url', 'update', 'created')


class LinkSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка ссылок"""
    class Meta:
        model = Link
        fields = '__all__'
