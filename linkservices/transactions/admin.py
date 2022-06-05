from django.contrib import admin

from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'balance_after_transaction', 'timestamp', 'transaction_type')
    readonly_fields = ('account', 'balance_after_transaction', 'transaction_type', 'amount', )
    list_select_related = ['account__user', ]


admin.site.register(Transaction, TransactionAdmin)
