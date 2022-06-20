from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django_filters.views import FilterView
from site_app.models import WebSite
from django.shortcuts import render

from .filters import SiteFilter
from .models import Plugin, Help


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


def frontpage(request):
    """Страница перед входом в аккаунт"""
    if request.user.is_authenticated:
        user_id = request.user.pk
        return HttpResponseRedirect(f'/profile/id={user_id}', locals())
    else:
        help = Help.objects.filter(main=True)
        return render(request, 'main/frontpage.html', {'help': help})
