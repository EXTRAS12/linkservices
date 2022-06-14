from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests

from .models import Event
from users.models import Profile


@receiver(post_save, sender=Event)
def send_event(sender, instance, *args, created, **kwargs):
    """Рассылка сообщений в телеграмм"""
    if created:
        if instance.all:
            for item in Profile.objects.all():
                chat_id = item.chat_id
                api_key = settings.API
                msg = instance.text
                text = f'{msg}'
                url = f'https://api.telegram.org/bot{api_key}/sendMessage'
                params = {
                    'chat_id': chat_id,
                    'text': text,
                }
                requests.get(url, params=params).json()

        elif instance.web:
            for web in Profile.objects.all():
                if web.user_website.count() > 0:
                    chat_id = web.chat_id
                    api_key = settings.API
                    msg = instance.text
                    text = f'{msg}'
                    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()

        elif instance.web:
            for link in Profile.objects.all():
                if link.user_link.count() > 0:
                    chat_id = link.chat_id
                    api_key = settings.API
                    msg = instance.text
                    text = f'{msg}'
                    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()

