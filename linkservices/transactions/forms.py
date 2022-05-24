import datetime

from django import forms
from django.conf import settings

from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)

        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.current_balance
        return super().save()


class DepositForm(TransactionForm):
    """Пополнения баланса"""
    def clean_amount(self):
        min_deposit_amount = settings.MINIMUM_DEPOSIT_AMOUNT
        amount = self.cleaned_data.get('amount')

        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'Минимальный депозит {min_deposit_amount} руб. '
            )

        return amount


class WithdrawForm(TransactionForm):
    """Вывод средств"""
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = settings.MINIMUM_WITHDRAWAL_AMOUNT

        balance = account.current_balance

        amount = self.cleaned_data.get('amount')

        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'Минимальный вывод {min_withdraw_amount} руб.'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'У вас {balance} руб. на аккаунте '
                'Вы не можете снять больше чем у вас имеется'
            )

        return amount

