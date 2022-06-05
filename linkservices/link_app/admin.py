from django.contrib import admin
from django import forms
from .models import VerifyStatus, Moderation, Link


class ModerationAdmin(admin.ModelAdmin):
    """Статус модерации"""
    list_display = ('id', 'name')


class VerifyStatusAdmin(admin.ModelAdmin):
    """Статус проверки"""
    list_display = ('id', 'name')


class LinkAdmin(admin.ModelAdmin):
    """Ссылки"""
    fields = ('url', 'user', 'link', 'status_verify', 'moderation',
              'count_month', 'valid_date', 'created', 'update')
    list_display = ('url', 'user', 'valid_date', 'total_increase_price', 'status_verify', 'moderation', 'created',
                    'update')
    search_fields = ('url__url', )
    list_filter = ('url', 'status_verify', 'moderation', 'valid_date', 'created', 'update')
    readonly_fields = ('url', 'user', 'created', 'update', 'valid_date')
    list_select_related = ['user__user', 'url', 'status_verify', 'moderation', ]
    # raw_id_fields = ['user', 'url']

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
