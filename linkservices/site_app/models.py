from django.db import models
from django.urls import reverse

from users.models import Profile


class Category(models.Model):
    """Тематика сайта"""
    name = models.CharField(max_length=200, verbose_name='Тематика')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'
        ordering = ('name',)


class Status(models.Model):
    """Статус"""
    name = models.CharField(max_length=155, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ('name',)


class WebSite(models.Model):
    """Модель добавления сайта"""
    url = models.CharField(max_length=255, verbose_name='url сайта')
    user_email = models.ForeignKey(Profile, related_name='user_website', on_delete=models.CASCADE,
                                   max_length=100, blank=True, null=True, verbose_name='email заказчика')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Тематика')
    price = models.IntegerField(verbose_name='Цена')
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, blank=True, null=True)
    total_link = models.IntegerField(verbose_name='Всего ссылок', blank=True, null=True)
    sold_link = models.IntegerField(verbose_name='Продано ссылок', blank=True, null=True)
    yandex_x = models.IntegerField(verbose_name='Яндекс Икс', blank=True, null=True)
    yandex_stat = models.CharField(max_length=255, verbose_name='Яндекс статистика')
    password_yandex = models.CharField(max_length=250, verbose_name='Пароль от статистики', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('buy-link', kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #     price_per_item = self.url.price
    #     self.price_per_item = price_per_item
    #     self.total_price = self.count_month * price_per_item
    #
    #     super(WebSite, self).save(*args, **kwargs)
