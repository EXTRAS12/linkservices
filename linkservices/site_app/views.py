from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, UpdateView
from django import forms

from .forms import AddSiteForm
from .models import WebSite


class MySites(LoginRequiredMixin, ListView):
    """Страница мои сайты"""
    template_name = 'site_app/mysites.html'
    model = WebSite
    context_object_name = 'website'
    paginate_by = 10

    def get_queryset(self):
        return WebSite.objects.filter(user=self.request.user.profile). \
            select_related('category', 'status')


class UpdateSite(LoginRequiredMixin, UpdateView):
    """Редактирование сайта"""
    model = WebSite
    form_class = AddSiteForm
    context_object_name = 'website'
    template_name = 'site_app/update-site.html'
    success_url = '/my-sites/'

    def form_valid(self, form):
        if self.object.total_link < self.object.get_total_link():
            messages.error(self.request, 'Вы не можете указать меньше доступных ссылок,'
                                         ' чем уже куплено!')
            return HttpResponseRedirect("")
        self.object = form.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """ Пользователь может редактировать только свои сайты """
        obj = self.get_object()
        if obj.user != self.request.user.profile:
            return redirect(obj)
        return super(UpdateSite, self).dispatch(request, *args, **kwargs)


class RemoveSite(LoginRequiredMixin, View):
    """Удаление сайта"""

    def get(self, request, pk):
        WebSite.objects.get(id=pk, user=self.request.user.profile).delete()
        messages.success(request, 'Ваш сайт успешно удалён')
        return redirect("my-sites")


@login_required
def add_site(request):
    """Добавления сайта"""
    form = AddSiteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.user = request.user.profile
            new_site.save()
            messages.success(request, 'Ваш сайт успешно добавлен!')
            return redirect('my-sites')
    return render(request, 'site_app/add-site.html', locals())
