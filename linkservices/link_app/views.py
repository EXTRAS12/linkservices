from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from site_app.models import WebSite

from .models import Link


class MyLinks(LoginRequiredMixin, ListView):
    """Страница мои ссылки"""
    model = Link
    template_name = 'link_app/mylinks.html'
    context_object_name = 'link'


class BuyLink(LoginRequiredMixin, DetailView):
    """Страница покупки ссылки"""
    model = WebSite
    template_name = 'link_app/buy-links.html'
    context_object_name = 'link'
