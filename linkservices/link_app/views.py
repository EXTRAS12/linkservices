from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, UpdateView

from .forms import AddLinkForm
from .models import Link
from site_app.models import WebSite

from transactions.models import Transaction
from transactions.constants import WITHDRAWAL, PURCHASE, TRANSFER


class MyLinks(LoginRequiredMixin, ListView):
    """Страница мои ссылки"""
    model = Link
    template_name = 'link_app/mylinks.html'
    context_object_name = 'link'
    paginate_by = 10

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user.profile).select_related()


class BuyLink(LoginRequiredMixin, FormMixin, DetailView):
    """Страница покупки ссылки"""
    model = WebSite
    form_class = AddLinkForm
    template_name = 'link_app/buy-links.html'
    success_url = '/catalog/'

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            month = form.cleaned_data.get('count_month')

            price = WebSite.objects.get(pk=self.kwargs.get('pk'))

            total = month * price.price
            if total > self.request.user.profile.current_balance:
                messages.error(request, 'Недостаточно средств на балансе')
                return HttpResponseRedirect(reverse_lazy('buy-link',  kwargs={'pk': price.pk}))

            else:
                self.request.user.profile.current_balance -= total
                self.request.user.profile.save(update_fields=['current_balance'])

                reciever = WebSite.objects.get(pk=self.kwargs.get('pk'))
                reciever.user.hold_balance = reciever.user.hold_balance + total
                reciever.user.save(update_fields=['hold_balance'])

                return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):

        form.save()
        return super(BuyLink, self).form_valid(form)


class UpdateLink(LoginRequiredMixin, UpdateView):
    """Редактирование ссылки"""
    form_class = AddLinkForm
    model = Link
    template_name = 'link_app/update-link.html'
    success_url = '/catalog/'
    context_object_name = 'link'

    def dispatch(self, request, *args, **kwargs):
        """ Пользователь может редактировать только свои ссылки """
        obj = self.get_object()
        if obj.user != self.request.user.profile:
            return redirect(obj)
        return super(UpdateLink, self).dispatch(request, *args, **kwargs)


@receiver(post_save, sender=Link)
def create_transactions(sender, instance, created, **kwargs):
    """Сохранение транзакций при покупке ссылки"""
    if created:
        Transaction.objects.create(account=instance.user,
                                   amount=instance.total_price,
                                   detail_pay=instance.url,
                                   timestamp=instance.created,
                                   transaction_type=PURCHASE)
        Transaction.objects.create(account=instance.url.user,
                                   amount=instance.total_price,
                                   detail_pay=instance.url,
                                   timestamp=instance.created,
                                   transaction_type=TRANSFER)
