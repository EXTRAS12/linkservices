from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from transactions.constants import DEPOSIT, WITHDRAWAL
from transactions.forms import (
    DepositForm,
    WithdrawForm,
)
from transactions.models import Transaction


class TransactionRepostView(LoginRequiredMixin, ListView):
    """Статистика пополнение/снятие"""
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    form_data = {}

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.profile
        )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.profile,
        })

        return context


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    """Снятие и пополнение баланса"""
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transactions:transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.profile
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    """Пополнение баланса"""
    form_class = DepositForm
    title = 'Пополнение баланса'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.profile

        account.current_balance += amount
        account.save(
            update_fields=[

                'current_balance',

            ]
        )

        messages.success(
            self.request,
            f'{amount}руб. успешно зачислено'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    """Вывод с баланса"""
    form_class = WithdrawForm
    title = 'Вывод средств с баланса'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')

        self.request.user.profile.current_balance -= form.cleaned_data.get('amount')
        self.request.user.profile.save(update_fields=['current_balance'])

        messages.success(
            self.request,
            f'Успешный вывод {amount}руб.'
        )

        return super().form_valid(form)
