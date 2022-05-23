from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django_filters.views import FilterView
from site_app.models import WebSite

from .filters import SiteFilter
from .models import Plugin, GeneralHelp


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'
    context_object_name = 'website'


class Help(LoginRequiredMixin, ListView):
    """Страница помощи"""
    model = GeneralHelp
    template_name = 'main/help.html'
    context_object_name = 'help'


class Catalog(LoginRequiredMixin, FilterView, ListView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'
    context_object_name = 'website'
    paginate_by = 15
    filterset_class = SiteFilter

    def get_queryset(self):
        return WebSite.objects.filter(status__name='Опубликовано').select_related('category')\
            .exclude(user_email=self.request.user.profile)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Catalog, self).get_context_data(**kwargs)
        context['title'] = 'Каталог сайтов'
        return context


class Plugins(LoginRequiredMixin, ListView):
    """Каталог плагинов"""
    model = Plugin
    template_name = 'main/plugins.html'
    context_object_name = 'plugins'
    paginate_by = 15
