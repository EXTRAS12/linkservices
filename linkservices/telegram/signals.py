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
        api_key = settings.API
        msg = instance.text
        text = f'{msg}'
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        for item in Profile.objects.all():
            if instance.all:
                chat_id = item.chat_id
                params = {
                    'chat_id': chat_id,
                    'text': text,
                }
                requests.get(url, params=params).json()

            elif instance.web:
                if item.user_website.count() > 0:
                    chat_id = item.chat_id

                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()

            elif instance.seo:
                if item.user_link.count() > 0:
                    chat_id = item.chat_id
                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()
