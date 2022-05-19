from rest_framework import generics
from django.shortcuts import render

from site_app.models import WebSite
from api.serializers import WebSiteSerializer
from link_app.models import Link
from api.serializers import LinkSerializer


class SiteApiView(generics.ListAPIView):
    """Апи для получения списка сайтов"""
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer


class LinkApiView(generics.ListAPIView):
    """Апи для получения списка ссылок"""
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
