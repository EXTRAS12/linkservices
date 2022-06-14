from django.core.mail import send_mail
from config.celery import app
from users.models import Profile

from django.conf import settings
import requests

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


# @app.task
# def send_telegram_msg():
#     for users in Profile.objects.all():
#         chat_id = users.chat_id
#         print(users)
#         print(chat_id)
#         api_key = settings.API
#         text = f'Какое то сообщение'
#         url = f'https://api.telegram.org/bot{api_key}/sendMessage'
#         params = {
#             'chat_id': chat_id,
#             'text': text,
#         }
#         requests.get(url, params=params).json()
