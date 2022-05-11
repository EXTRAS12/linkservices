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
    fields = ('url', 'user_email', 'link', 'status_verify', 'moderation', 'valid_date', 'created', 'update')
    list_display = ('url', 'user_email', 'valid_date', 'status_verify', 'moderation',  'created',
                    'update')
    search_fields = ('url', 'user_email', 'link')
    list_filter = ('url', 'status_verify', 'moderation', 'valid_date', 'created', 'update')
    readonly_fields = ('created', 'update')


admin.site.register(Moderation, ModerationAdmin)
admin.site.register(VerifyStatus, VerifyStatusAdmin)
admin.site.register(Link, LinkAdmin)
