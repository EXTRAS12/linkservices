from django.db import models

from .constants import TRANSACTION_TYPE_CHOICES
from users.models import Profile


class Transaction(models.Model):
    """Модель транзакций"""
    account = models.ForeignKey(Profile, related_name='transactions',
                                on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Количество')
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12,
                                                    verbose_name='Баланс после транзакции')
    transaction_type = models.PositiveIntegerField(choices=TRANSACTION_TYPE_CHOICES,
                                                   verbose_name='Тип транзакции')
    detail_pay = models.CharField(max_length=250, blank=True, null=True, verbose_name='Детали платежа')
    timestamp = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return str(self.account)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'


