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


class WebSite(models.Model):
    """Модель добавления сайта"""
    MODERATION = 'На модерации'
    PUBLISHED = 'Опубликовано'
    REJECTED = 'Отклонено'
    STATUS_CHOICES = (
        (MODERATION, 'На модерации'),
        (PUBLISHED, 'Опубликовано'),
        (REJECTED, 'Отклонено')
    )
    url = models.CharField(max_length=255, verbose_name='url сайта')
    user = models.ForeignKey(Profile, related_name='user_website', on_delete=models.CASCADE,
                             max_length=100, blank=True, null=True, verbose_name='email заказчика')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Тематика')
    price = models.IntegerField(verbose_name='Цена')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=MODERATION, verbose_name='Статус')
    total_link = models.IntegerField(verbose_name='Всего ссылок', blank=True, null=True)
    yandex_x = models.IntegerField(verbose_name='Яндекс Икс', blank=True, null=True)
    yandex_stat = models.CharField(max_length=255, verbose_name='Яндекс статистика')
    increase = models.PositiveIntegerField(verbose_name='Наценка %', default=50, blank=True, null=True)
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

    def get_increase_price(self):
        """Цена с наценкой"""
        return int(self.price * (self.increase / 100 + 1))

    @property
    def get_total_link(self):
        return self.link_set.count()
