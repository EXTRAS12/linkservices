from django.conf import settings
from django.shortcuts import render, redirect
from django.db import IntegrityError
from uuid import uuid4
from django.db.models.signals import post_save
import requests
from site_app.models import WebSite
from .forms import *


# def main(request):
#     if request.method == 'POST':
#         form = Request(request.POST)
#         if form.is_valid():
#             TOKEN = str(uuid4())
#             cd = form.cleaned_data
#             r = Requests(name=cd['name'],
#                          type=cd['type'],
#                          request=cd['request'],
#                          email=cd['email'],
#                          TOKEN=TOKEN)
#             r.save()
#             Requests.objects.update()
#             try:
#                 UserRequest.objects.create(name=cd['name'], email=cd['email'])
#             except IntegrityError:
#                 pass
#             return redirect(f'https://t.me/bot_broken_bot?start={TOKEN}')
#
#     else:
#         form = Request()
#     return render(request, 'main.html', {'form': form})


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
