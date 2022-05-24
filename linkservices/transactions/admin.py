from django.contrib import admin

from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'balance_after_transaction', 'timestamp', 'transaction_type')


admin.site.register(Transaction, TransactionAdmin)
