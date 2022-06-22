from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transaction


# @receiver(post_save, sender=Transaction)
# def send_updates_status_transaction(sender, update_fields, instance, **kwargs):
#     """Уведомляем пользователя о статусе ссылки"""
#     if update_fields is not None:
#         status = 'status'
#         if status in update_fields:
#             print(instance.account.user.profile)
#             print(instance.amount)
#             user = instance.account.output_balance - int(instance.amount)
#             print(user)
#
#             instance.account.save(update_fields=['output_balance'])


