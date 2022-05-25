from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from django.core.files import File
from io import BytesIO
from PIL import Image


class User(AbstractUser):
    """Основной юзер"""
    email = models.EmailField(_("email address"), unique=True, )

    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ('-date_joined',)


class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(User, verbose_name="Пользователь",
                                related_name='profile', null=True, on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Чат ID телеграмм')
    TOKEN = models.CharField(max_length=100, blank=True, null=True)
    wmz = models.CharField(max_length=200, blank=True, null=True, verbose_name='WMZ-кошелёк')
    ymoney = models.CharField(max_length=200, blank=True, null=True, verbose_name='ЮMoney-кошелёк')
    current_balance = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name="Текущий баланс")
    hold_balance = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='На удержании')
    output_balance = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Ожидает вывода')
    name_telegram = models.CharField(blank=True, null=True, max_length=100, verbose_name='Телеграмм')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', blank=True, null=True, verbose_name='Аватар')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    """При регистрации создаётся профиль пользователя"""
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
