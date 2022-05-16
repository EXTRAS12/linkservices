from django.conf import settings
from django.db.models.signals import post_save
import requests

from site_app.models import WebSite
from link_app.models import Link


def send_updates_status(sender, update_fields, instance, **kwargs):
    """Уведомляем пользователя о статусе сайта"""
    if update_fields is not None:
        sta = 'status'
        if sta in update_fields:
            status = instance.status
            url = instance.url
            chat_id = instance.bot_id
            # status = instance.status
            api_key = settings.API
            # chat_id = str(instance.bot_id)
            text = f'Статус вашего сайта изменился: {url} ' + str(status)
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
        if sta in update_fields:
            status = instance.status_verify
            chat_id = instance.bot_id
            # status = instance.status
            api_key = settings.API
            # chat_id = str(instance.bot_id)
            text = f'Статус вашей ссылки: ' + str(status)
            url = f'https://api.telegram.org/bot{api_key}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': text,
            }
            return requests.get(url, params=params).json()


# Соединяем с сигналом
post_save.connect(send_updates_status, sender=WebSite)
post_save.connect(send_updates_status_link, sender=Link)
