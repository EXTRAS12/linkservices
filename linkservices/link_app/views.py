from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import AddLinkForm
from .models import Link


class MyLinks(LoginRequiredMixin, ListView):
    """Страница мои ссылки"""
    model = Link
    template_name = 'link_app/mylinks.html'
    context_object_name = 'link'
    paginate_by = 15

    def get_queryset(self):
        return Link.objects.filter(user_email=self.request.user.profile)


class BuyLink(LoginRequiredMixin, FormView):
    """Страница покупки ссылки"""
    form_class = AddLinkForm
    template_name = 'link_app/buy-links.html'
    success_url = '/catalog/'

    def get_context_data(self, **kwargs):

        context = super(BuyLink, self).get_context_data(**kwargs)
        context['link'] = Link.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.save()
        return super(BuyLink, self).form_valid(form)
