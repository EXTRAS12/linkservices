from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .forms import AddSiteForm
from .models import WebSite


class MySites(LoginRequiredMixin, ListView):
    """Страница мои сайты"""
    template_name = 'site_app/mysites.html'
    model = WebSite
    context_object_name = 'website'
    paginate_by = 15

    def get_queryset(self):
        return WebSite.objects.filter(user_email=self.request.user.profile).\
            select_related('category', 'status')


class UpdateSite(LoginRequiredMixin, UpdateView):
    """Редактирование сайта"""
    model = WebSite
    form_class = AddSiteForm
    context_object_name = 'website'
    template_name = 'site_app/add-site.html'
    success_url = '/my-sites/'

    def dispatch(self, request, *args, **kwargs):
        """ Пользователь может редактировать только свои сайты """
        obj = self.get_object()
        if obj.user_email != self.request.user.profile:
            return redirect(obj)
        return super(UpdateSite, self).dispatch(request, *args, **kwargs)


class DeleteSite(LoginRequiredMixin, DeleteView):
    """Удаление сайта"""
    model = WebSite
    success_url = reverse_lazy('my-sites')

    def dispatch(self, request, *args, **kwargs):
        """ Пользователь может удалять только свои сайты """
        obj = self.get_object()
        if obj.user_email != self.request.user.profile:
            return redirect(obj)
        return super(DeleteSite, self).dispatch(request, *args, **kwargs)


@login_required
def add_site(request):
    """Добавления сайта"""
    form = AddSiteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.user_email = request.user.profile
            new_site.save()
            return redirect('my-sites')
    return render(request, 'site_app/add-site.html', locals())
