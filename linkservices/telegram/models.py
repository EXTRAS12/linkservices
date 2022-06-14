from django.db import models
from users.models import Profile


class Event(models.Model):
    name = models.CharField(max_length=150,blank=True, null=True, verbose_name="Название")
    text = models.TextField(verbose_name="Сообщение")
    all = models.BooleanField(verbose_name='Отправить всем', default=None)
    web = models.BooleanField(verbose_name='Вебмастерам', default=None)
    seo = models.BooleanField(verbose_name='Сео специалистам', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылку'
        verbose_name_plural = 'Рассылки'
