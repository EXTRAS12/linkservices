from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Category, WebSite
from .forms import AddSiteForm


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'


class Profile(LoginRequiredMixin, TemplateView):
    """Профиль"""
    template_name = 'main/profile.html'


class MySites(LoginRequiredMixin, ListView):
    """Страница мои сайты"""
    template_name = 'main/mysites.html'
    model = WebSite
    context_object_name = 'website'

    def get_queryset(self):
        return WebSite.objects.filter(user_email=self.request.user)


class MyLinks(LoginRequiredMixin, TemplateView):
    """Страница мои ссылки"""
    template_name = 'main/mylinks.html'


class AddLink(LoginRequiredMixin, TemplateView):
    """Страница добавления ссылок"""
    template_name = 'main/add-links.html'


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


class Plugins(LoginRequiredMixin, TemplateView):
    """Каталог сайтов"""
    template_name = 'main/plugins.html'


@login_required
def add_site(request):
    """Добавления сайта"""
    form = AddSiteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.user_email = request.user
            new_site.save()
            return redirect('my-sites')
    return render(request, 'main/add-site.html', locals())
