from config.celery import app
from link_app.models import Link
from django.utils import timezone
import datetime


@app.task
def balance_transfer():
    """Для теста"""
    for balance in Link.objects.filter(valid_date__gt=datetime.datetime.now()):
        if balance.user.hold_balance > 1000 and balance.valid_date > timezone.now():

            balance.user.hold_balance -= balance.url.price
            balance.user.save(update_fields=['hold_balance'])
            balance.user.current_balance += balance.url.price
            balance.user.save(update_fields=['current_balance'])
