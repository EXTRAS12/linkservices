from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем слать вам много спама.',
        'info.moonshine@yandex.ru',
        [user_email, ],
        fail_silently=False,
    )
