from users.models import Profile, User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4


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