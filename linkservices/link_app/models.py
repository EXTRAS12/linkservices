from django.db import models
from django.utils import timezone

from site_app.models import WebSite

from users.models import Profile


class Link(models.Model):
    """Модель для ссылки"""
    CHECKED = 'Проверено'
    REVIEW = 'На проверке'
    PUBLISHED = 'Отображается'
    STATUS_CHOICE = (
        (CHECKED, 'Проверено'),
        (REVIEW, 'На проверке'),
        (PUBLISHED, 'Отображается')

    )
    url = models.ForeignKey(WebSite, on_delete=models.CASCADE, verbose_name='url сайта')
    link = models.TextField(verbose_name="Ссылка")
    status_verify = models.CharField(max_length=25, choices=STATUS_CHOICE, default=REVIEW,
                                     verbose_name='Статус проверки')
    moderation = models.CharField(max_length=25, choices=STATUS_CHOICE, default=REVIEW,
                                  verbose_name='Статус модерации')
    valid_date = models.DateTimeField(auto_now_add=False, verbose_name='В работе до', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    user = models.ForeignKey(Profile, related_name='user_link', on_delete=models.CASCADE,
                             max_length=100, blank=True, null=True, verbose_name='email заказчика')
    count_month = models.IntegerField(default=1, verbose_name='Количество месяцев')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ('-created',)

    def total_increase_price(self):
        """Общая сумма с наценкой"""
        return self.url.get_increase_price() * int(self.count_month)

    def total_price(self):
        """Общая сумма без наценки"""
        return self.url.price * int(self.count_month)

    def get_amount_saved(self):
        return self.total_increase_price() - self.total_price()

    def save(self, *args, **kwargs):
        """При сохранении считается общая сумма"""

        count_month = self.count_month
        self.valid_date = timezone.now() + timezone.timedelta(days=30) * int(count_month)
        super(Link, self).save(*args, **kwargs)
