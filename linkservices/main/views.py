from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from site_app.models import WebSite

from users.models import Profile

from .models import Plugin


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'
    context_object_name = 'website'


class ProfileView(LoginRequiredMixin, TemplateView):
    """Профиль"""
    model = Profile
    template_name = 'main/profile.html'


class Help(LoginRequiredMixin, TemplateView):
    """Страница помощи"""
    template_name = 'main/help.html'


class Catalog(LoginRequiredMixin, ListView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'
    context_object_name = 'website'

    def get_queryset(self):
        return WebSite.objects.filter(status_id=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Catalog, self).get_context_data(**kwargs)
        context['title'] = 'Каталог сайтов'
        return context


class Plugins(LoginRequiredMixin, ListView):
    """Каталог плагинов"""
    model = Plugin
    template_name = 'main/plugins.html'
    context_object_name = 'plugins'
