from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Category, WebSite
from .forms import AddSiteForm


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'


class Profile(TemplateView):
    """Профиль"""
    template_name = 'main/profile.html'


class MySites(TemplateView):
    """Страница мои сайты"""
    template_name = 'main/mysites.html'


class AddSite(CreateView):
    """Страница добавления сайтов"""
    model = WebSite
    context_object_name = 'website'
    template_name = 'main/add-site.html'
    form_class = AddSiteForm
    success_url = reverse_lazy('my-sites')


class MyLinks(TemplateView):
    """Страница мои ссылки"""
    template_name = 'main/mylinks.html'


class AddLink(TemplateView):
    """Страница добавления ссылок"""
    template_name = 'main/add-links.html'


class Help(TemplateView):
    """Страница помощи"""
    template_name = 'main/help.html'


class Catalog(ListView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'
    context_object_name = 'website'

    def get_queryset(self):
        return WebSite.objects.filter(id=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Catalog, self).get_context_data(**kwargs)
        context['title'] = 'Каталог сайтов'
        return context


class Plugins(TemplateView):
    """Каталог сайтов"""
    template_name = 'main/plugins.html'
