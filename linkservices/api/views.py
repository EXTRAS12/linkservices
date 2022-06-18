from rest_framework import generics

from site_app.models import WebSite
from api.serializers import WebSiteSerializer, LinkSerializer, DetailSiteSerializer
from link_app.models import Link


class SiteApiView(generics.ListAPIView):
    """Апи для получения списка сайтов"""
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer


class LinkApiView(generics.ListAPIView):
    """Апи для получения списка ссылок"""
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class DetailSite(generics.RetrieveAPIView):
    serializer_class = DetailSiteSerializer
    queryset = WebSite.objects.all()

