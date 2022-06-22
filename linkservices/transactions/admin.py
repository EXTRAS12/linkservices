from django.contrib import admin

from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'status', 'transaction_type', 'timestamp')
    readonly_fields = ('account', 'balance_after_transaction', 'transaction_type', 'amount', )
    list_filter = ('transaction_type', 'status')
    list_select_related = ['account__user', ]

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для транзакции"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        super(TransactionAdmin, self).save_model(request, obj, form, change)
        obj.save(update_fields=update_fields)


admin.site.register(Transaction, TransactionAdmin)
