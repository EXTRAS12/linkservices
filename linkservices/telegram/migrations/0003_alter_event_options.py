# Generated by Django 4.0.4 on 2022-06-16 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_event_all_event_seo_event_web'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Рассылку', 'verbose_name_plural': 'Рассылки'},
        ),
    ]