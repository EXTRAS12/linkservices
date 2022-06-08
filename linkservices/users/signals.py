from django.conf import settings
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4

from users.models import Profile, User


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    """При регистрации создаётся профиль пользователя"""
    TOKEN = str(uuid4())
    if created:
        Profile.objects.create(user=instance,
                               TOKEN=TOKEN)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance,
                                   TOKEN=TOKEN)


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
