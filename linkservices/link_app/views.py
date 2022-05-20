from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import AddLinkForm
from .models import Link
from site_app.models import WebSite


class MyLinks(LoginRequiredMixin, ListView):
    """Страница мои ссылки"""
    model = Link
    template_name = 'link_app/mylinks.html'
    context_object_name = 'link'
    paginate_by = 15

    def get_queryset(self):
        return Link.objects.filter(user_email=self.request.user.profile).select_related()


class BuyLink(LoginRequiredMixin, FormMixin, DetailView):
    """Страница покупки ссылки"""
    model = WebSite
    form_class = AddLinkForm
    template_name = 'link_app/buy-links.html'
    success_url = '/catalog/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BuyLink, self).form_valid(form)
