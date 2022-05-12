from django.conf import settings
from django.db.models.signals import post_save
import requests

from site_app.models import WebSite


def send_updates_status(sender, update_fields, instance, **kwargs):
    """Уведомляем пользователя о статусе заявки"""
    if update_fields is not None:
        sta = 'status'
        if sta in update_fields:
            status = instance.status
            chat_id = instance.bot_id
            # status = instance.status
            api_key = settings.API
            # chat_id = str(instance.bot_id)
            text = 'Статус вашей заявки изменился: ' + str(status)
            url = f'https://api.telegram.org/bot{api_key}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': text,
            }
            return requests.get(url, params=params).json()


# Соединяем с сигналом
post_save.connect(send_updates_status, sender=WebSite)

