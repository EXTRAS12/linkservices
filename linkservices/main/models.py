from django.db import models
from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.fields import RichTextUploadingField


class NewFlatpage(models.Model):
    """Модель для статических страниц"""
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    description = RichTextUploadingField(verbose_name='Основной текстовый контент страницы', default='')
    text_block = RichTextUploadingField(verbose_name='Дополнительный блок текста', default='')

    def __str__(self):
        return self.flatpage.title

    class Meta:
        verbose_name = "Содержание страницы"
        verbose_name_plural = "Содержание страниц"


class Plugin(models.Model):
    """Модель для плагинов"""
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание')
    version = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name='Версия')
    instruction = models.TextField(verbose_name='Инструкция', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='icon_plugins/%Y/%m/%d/', verbose_name='Иконка плагина', blank=True)
    file = models.FileField(upload_to='plugins/%Y/%m/%d/', verbose_name='Плагин')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Плагин"
        verbose_name_plural = "Плагины"


class Stat(models.Model):
    """Модель статистики в системе"""
    balance_for_all_time = models.PositiveIntegerField(default=0, blank=True,
                                                       null=True, verbose_name="Заработано за всё время")
    balance_current = models.PositiveIntegerField(default=0, blank=True,
                                                  null=True, verbose_name="Заработано на текущий момент")
    balance_hold = models.PositiveIntegerField(default=0, blank=True,
                                               null=True, verbose_name="На удержании")
    update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

