from django.db.models.signals import pre_save
from django.dispatch import receiver
from transactions.models import Transaction


@receiver(pre_save, sender=Transaction)
def send_updates_status_transaction(sender, update_fields, instance, **kwargs):
    """Вывод средств когда статус меняется на выполнено деньги снимаются с "Ожидает вывода" """
    if update_fields is not None:
        status = 'status'
        if status in update_fields:
            if instance.status == 'Выполнено':

                instance.account.output_balance -= int(instance.amount)
                instance.account.save(update_fields=['output_balance'])
