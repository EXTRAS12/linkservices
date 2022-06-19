from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch, Count
from django.views.generic import ListView
from django_filters.views import FilterView
from site_app.models import WebSite

from .filters import SiteFilter
from .models import Plugin, Help


class FrontPage(ListView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'
    model = Help
    context_object_name = 'help'
    queryset = Help.objects.filter(main=True)


class HelpView(LoginRequiredMixin, ListView):
    """Страница помощи"""
    template_name = 'main/help.html'
    model = Help
    context_object_name = 'help'


class Catalog(LoginRequiredMixin, FilterView, ListView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'
    context_object_name = 'website'
    paginate_by = 10
    model = WebSite
    filterset_class = SiteFilter

    def get_queryset(self):
        return WebSite.objects.filter(status='Опубликовано')\
            .select_related('category').exclude(user=self.request.user.profile)\
            .prefetch_related(Prefetch('link_set'))

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
