from django.conf import settings
import requests
from django.dispatch import receiver
from django.db.models.signals import post_save

from site_app.models import WebSite


def send_updates_status(sender, update_fields, instance, **kwargs):
    """Уведомляем пользователя о статусе сайта"""
    if update_fields is not None:
        sta = 'status'
        if sta in update_fields:
            status = instance.status
            url = instance.url
            chat_id = instance.user.chat_id
            api_key = settings.API
            text = f'Статус вашего сайта "{url}" изменился:  ' + str(status)
            url = f'https://api.telegram.org/bot{api_key}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': text,
            }
            return requests.get(url, params=params).json()


@receiver(post_save, sender=WebSite)
def add_new_site(sender, instance, created, *args, **kwargs):
    """Уведомление при добавлении нового сайта"""
    if created:
        website = instance.url
        site_id = instance.id
        chat_id = settings.MY_BOT_ID  # надо указать айди админ чата
        api_key = settings.API
        text = f'Добавлен новый сайт: id({site_id}) ' + str(website)
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        return requests.get(url, params=params).json()


#  Соединяем с сигналом
post_save.connect(send_updates_status, sender=WebSite)
