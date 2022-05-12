# Generated by Django 4.0.4 on 2022-05-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тематика')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='url сайта')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('total_link', models.IntegerField(blank=True, null=True, verbose_name='Всего ссылок')),
                ('sold_link', models.IntegerField(blank=True, null=True, verbose_name='Продано ссылок')),
                ('yandex_x', models.IntegerField(blank=True, null=True, verbose_name='Яндекс Икс')),
                ('yandex_stat', models.CharField(max_length=255, verbose_name='Яндекс статистика')),
                ('password_yandex', models.CharField(blank=True, max_length=250, null=True, verbose_name='Пароль от статистики')),
                ('bot_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.category', verbose_name='Тематика')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_app.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
                'ordering': ('-created',),
            },
        ),
    ]
