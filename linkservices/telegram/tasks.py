from django.core.mail import send_mail
from config.celery import app

from users.models import Profile

from django.conf import settings
import requests

from .models import Event


@app.task
def send_event():
    """Рассылка в телеграмм"""
    for event in Event.objects.all():
        api_key = settings.API
        msg = event.text
        text = f'{msg}'
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        for item in Profile.objects.all():
            if event.all:
                chat_id = item.chat_id
                params = {
                    'chat_id': chat_id,
                    'text': text,
                }
                requests.get(url, params=params).json()
            elif event.web:
                if item.user_website.count() > 0:
                    chat_id = item.chat_id

                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()

            elif event.seo:
                if item.user_link.count() > 0:
                    chat_id = item.chat_id
                    params = {
                        'chat_id': chat_id,
                        'text': text,
                    }
                    requests.get(url, params=params).json()


# @app.task
# def send_beat_email():
#    """Массовая рассылка сообщений"""
#    for contact in Profile.objects.all():
#        send_mail(
#            'Пам парапам',
#            'Ловите спам!',
#            'info.moonshine@yandex.ru',
#            [contact.user.email],
#            fail_silently=False,
#        )
