# Generated by Django 4.0.4 on 2022-06-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_stat_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'verbose_name': 'Статистику', 'verbose_name_plural': 'Статистика'},
        ),
        migrations.AlterField(
            model_name='stat',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название(Статистика)'),
        ),
    ]
