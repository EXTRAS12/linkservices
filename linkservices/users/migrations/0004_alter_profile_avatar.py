# Generated by Django 4.0.4 on 2022-05-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/', verbose_name='Аватар'),
        ),
    ]
