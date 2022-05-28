import telebot
from django.conf import settings

from django.core.management.base import BaseCommand

from users.models import Profile


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        main()


bot = telebot.TeleBot(settings.API)


@bot.message_handler(func=lambda message: True)
def activate(message):
    qusetion = message.text
    qs = qusetion.split()
    if qs[0] == '/start':
        if len(qs) == 2:
            token = str(qs[1])
            try:
                obj = Profile.objects.get(TOKEN=token)
            except Profile.DoesNotExist:
                obj = None
                bot.reply_to(message, 'Не удалось привязать бота')
            if obj:
                print(obj)
                obj.chat_id = message.chat.id
                obj.save()
                # obj.update(bot_id=message.chat.id)
                bot.reply_to(message,
                             'Вы привязали бота, теперь вы будете получать уведомления')


def main():
    bot.polling()


if __name__ == '__main__':
    main()
