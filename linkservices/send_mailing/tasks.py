from django.core.mail import send_mail
from .celery import app

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


# циклом пачку писем
@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем слать вам письма каждые 5 минут.',
            'info.moonshine@yandex.ru',
            [contact.email, ],
            fail_silently=False,
        )
