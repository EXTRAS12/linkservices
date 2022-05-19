from django.contrib import admin
from .models import VerifyStatus, Moderation, Link


class ModerationAdmin(admin.ModelAdmin):
    """Статус модерации"""
    list_display = ('id', 'name')


class VerifyStatusAdmin(admin.ModelAdmin):
    """Статус проверки"""
    list_display = ('id', 'name')


class LinkAdmin(admin.ModelAdmin):
    """Ссылки"""
    fields = ('url', 'user_email', 'link', 'status_verify', 'moderation', 'total_price',
              'price_per_item', 'count_month', 'valid_date', 'created', 'update')
    list_display = ('url', 'user_email', 'valid_date', 'status_verify', 'moderation',  'created',
                    'update')
    search_fields = ('url', 'user_email', 'link')
    list_filter = ('url', 'status_verify', 'moderation', 'valid_date', 'created', 'update')
    readonly_fields = ('created', 'update', 'valid_date')

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для уведомления пользователя"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        super(LinkAdmin, self).save_model(request, obj, form, change)
        obj.save(update_fields=update_fields)


admin.site.register(Moderation, ModerationAdmin)
admin.site.register(VerifyStatus, VerifyStatusAdmin)
admin.site.register(Link, LinkAdmin)
