from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'


class Profile(TemplateView):
    """Профиль"""
    template_name = 'main/profile.html'


class MySites(TemplateView):
    """Страница мои сайты"""
    template_name = 'main/mysites.html'


class AddSite(TemplateView):
    """Страница добавления сайтов"""
    template_name = 'main/add-site.html'


class MyLinks(TemplateView):
    """Страница мои ссылки"""
    template_name = 'main/mylinks.html'


class AddLink(TemplateView):
    """Страница добавления ссылок"""
    template_name = 'main/add-links.html'


class Help(TemplateView):
    """Страница помощи"""
    template_name = 'main/help.html'


class Catalog(TemplateView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'


class Plugins(TemplateView):
    """Каталог сайтов"""
    template_name = 'main/plugins.html'
