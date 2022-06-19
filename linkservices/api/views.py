from django.db.models import Prefetch
from rest_framework import generics
import datetime

from rest_framework.generics import get_object_or_404

from site_app.models import WebSite
from api.serializers import WebSiteSerializer, LinkSerializer, DetailSiteSerializer, LinkSetSerializer
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
    """Для получения конкретного сайта"""
    serializer_class = DetailSiteSerializer

    def get_queryset(self):
        return WebSite.objects.prefetch_related(
            Prefetch('link_set', queryset=Link.objects.filter(valid_date__gte=datetime.datetime.now(),
                                                              status_verify='Отображается')))
