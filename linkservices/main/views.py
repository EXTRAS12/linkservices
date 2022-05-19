from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from site_app.models import WebSite

from users.models import Profile

from .forms import ProfileForm
from .models import Plugin


class FrontPage(TemplateView):
    """Страница перед входом в аккаунт"""
    template_name = 'main/frontpage.html'
    context_object_name = 'website'


class ProfileView(LoginRequiredMixin, DetailView):
    """Профиль"""
    model = Profile
    template_name = 'main/profile.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Редактирование профиля"""
    form_class = ProfileForm
    model = Profile
    template_name = "main/profile.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.instance.wmz)
        print(form.instance.ymoney)
        return super().form_invalid(form)


class Help(LoginRequiredMixin, TemplateView):
    """Страница помощи"""
    template_name = 'main/help.html'


class Catalog(LoginRequiredMixin, ListView):
    """Каталог сайтов"""
    template_name = 'main/catalog.html'
    context_object_name = 'website'
    paginate_by = 15

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
    paginate_by = 15
