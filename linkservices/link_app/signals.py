from django.db.models.signals import post_save
from django.dispatch import receiver

from transactions.models import Transaction
from transactions.constants import WITHDRAWAL, PURCHASE, TRANSFER
from link_app.models import Link


@receiver(post_save, sender=Link)
def create_transactions(sender, instance, created, **kwargs):
    """Сохранение транзакций при покупке ссылки"""
    if created:
        Transaction.objects.create(account=instance.user,
                                   amount=instance.total_increase_price(),
                                   detail_pay=instance.url,
                                   timestamp=instance.created,
                                   transaction_type=PURCHASE)
        Transaction.objects.create(account=instance.url.user,
                                   amount=instance.total_price(),
                                   detail_pay=instance.url,
                                   timestamp=instance.created,
                                   transaction_type=TRANSFER)


# @receiver(post_save, sender=Link)
# def after_update_link_create_transactions(sender, update_fields, instance, **kwargs):
#     """Сохранение транзакций после обновления ссылки"""
#     if update_fields is not None:
#         count_month = 'count_month'
#         if count_month in update_fields:
#             Transaction.objects.create(account=instance.user,
#                                        amount=instance.total_increase_price(),
#                                        detail_pay=instance.url,
#                                        timestamp=instance.created,
#                                        transaction_type=PURCHASE)
#             Transaction.objects.create(account=instance.url.user,
#                                        amount=instance.total_price(),
#                                        detail_pay=instance.url,
#                                        timestamp=instance.created,
#                                        transaction_type=TRANSFER)
