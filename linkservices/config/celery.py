import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # 'send-spam-every-2-minute': {
    #     'task': 'telegram.tasks.send_beat_email',
    #     'schedule': crontab(minute='*/10'),
    # },
    'send-telegram-msg': {
        'task': 'telegram.tasks.send_telegram_msg',
        'schedule': crontab(minute='*/2'),
    },
}
