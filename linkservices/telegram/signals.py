from django.conf import settings
from django.db.models.signals import post_save
import requests
from django.dispatch import receiver

from site_app.models import WebSite
from link_app.models import Link

from users.models import Profile


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


def send_updates_status_link(sender, update_fields, instance, **kwargs):
    """Уведомляем пользователя о статусе ссылки"""
    if update_fields is not None:
        sta = 'status_verify'
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


@receiver(post_save, sender=Profile)
def register_new_user(sender, instance, created, *args, **kwargs):
    """Уведомление при регистрации нового пользователя"""
    if created:
        user = instance.user.email
        chat_id = settings.MY_BOT_ID
        api_key = settings.API
        text = f'Зарегистрирован новый пользователь: ' + str(user)
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


@receiver(post_save, sender=Link)
def add_new_site(sender, instance, created, *args, **kwargs):
    """Уведомление покупка ссылки"""
    if created:
        link_url = instance.url
        link_user = instance.user
        chat_id = settings.MY_BOT_ID  # надо указать айди админ чата
        api_key = settings.API
        text = f'Куплена новая ссылка пользователем {link_user} на сайте {link_url}'
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        return requests.get(url, params=params).json()


# Соединяем с сигналом
post_save.connect(send_updates_status, sender=WebSite)
post_save.connect(send_updates_status_link, sender=Link)
