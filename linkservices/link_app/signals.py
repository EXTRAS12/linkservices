from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests

from transactions.models import Transaction
from transactions.constants import WITHDRAWAL, PURCHASE, TRANSFER, EXTENSION
from link_app.models import Link


@receiver(post_save, sender=Link)
def create_transactions(sender, instance, *args, created, **kwargs):
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

        chat_id = instance.url.user.chat_id
        api_key = settings.API
        amount = instance.total_price()
        text = f'Средства в размере {amount} были зачислены на удержание,' \
               f' ровно через месяц они будут зачислены на основной' \
               f' баланс и станут доступны для вывода'
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        return requests.get(url, params=params).json()


def send_updates_status_link(sender, update_fields, instance, **kwargs):
    """Уведомляем пользователя о статусе ссылки"""
    if update_fields is not None:
        sta = 'status_verify'
        lk = 'link'
        if sta in update_fields:
            status = instance.status_verify
            link_id = instance.id
            chat_id = instance.user.chat_id
            api_key = settings.API
            text = f'Ваша ссылка id{link_id} {status}'
            url = f'https://api.telegram.org/bot{api_key}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': text,
            }
            return requests.get(url, params=params).json()


@receiver(post_save, sender=Link)
def add_new_site(sender, instance, created, *args, **kwargs):
    """Уведомление покупка ссылки"""
    if created:
        link_url = instance.url
        link_user = instance.user
        chat_id = settings.MY_BOT_ID 
        api_key = settings.API
        text = f'Куплена новая ссылка пользователем {link_user} на сайте {link_url}'
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        return requests.get(url, params=params).json()


post_save.connect(send_updates_status_link, sender=Link)
