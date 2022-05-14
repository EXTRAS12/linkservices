# Generated by Django 4.0.4 on 2022-05-14 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='user_email',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_website', to=settings.AUTH_USER_MODEL, verbose_name='email заказчика'),
        ),
    ]
