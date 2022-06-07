# Generated by Django 4.0.4 on 2022-06-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0003_website_increase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('moderation', 'На модерации'), ('published', 'Опубликовано'), ('rejected', 'Отклонено')], default='moderation', max_length=20),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
