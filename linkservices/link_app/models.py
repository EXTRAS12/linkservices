from django.db import models
from django.utils import timezone

from site_app.models import WebSite
from users.models import User


def one_week_hence():
    """ссылка на 30 дней"""
    return timezone.now() + timezone.timedelta(days=30)


class VerifyStatus(models.Model):
    """Статус проверки для json """
    name = models.CharField(max_length=255, verbose_name='Статус проверки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус проверки'
        verbose_name_plural = 'Статусы проверок'
        ordering = ('name',)


class Moderation(models.Model):
    """Статус модерации"""
    name = models.CharField(max_length=255, verbose_name='Статус модерации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус модерации'
        verbose_name_plural = 'Статусы модерации'
        ordering = ('name',)


class Link(models.Model):
    """Модель для ссылки"""
    url = models.ForeignKey(WebSite, on_delete=models.CASCADE, verbose_name='url сайта')
    link = models.TextField(verbose_name="Ссылка")
    status_verify = models.ForeignKey(VerifyStatus, on_delete=models.CASCADE,
                                      verbose_name='Статус проверки', blank=True, null=True)
    moderation = models.ForeignKey(Moderation, on_delete=models.CASCADE,
                                   verbose_name='Статус модерации', blank=True, null=True)
    valid_date = models.DateTimeField(default=one_week_hence, verbose_name='В работе до')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    user_email = models.ForeignKey(User, on_delete=models.CASCADE,
                                   max_length=100, blank=True, null=True, verbose_name='email заказчика')
    price_per_item = models.IntegerField(default=0, verbose_name='Цена за 1 месяц')
    total_price = models.IntegerField(default=0, verbose_name='Общая стоимость')
    count_month = models.IntegerField(default=1, verbose_name='Количество месяцев')
    bot_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        price_per_item = self.url.price
        self.price_per_item = price_per_item
        self.total_price = self.count_month * price_per_item
        # self.valid_date = int(self.count_month) * timezone.timedelta(days=30) + self.valid_date
        super(Link, self).save(*args, **kwargs)
