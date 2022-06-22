from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    """Ссылки"""
    fields = ('url', 'user', 'link', 'link2', 'status_verify', 'moderation',
              'count_month', 'valid_date', 'created', 'update')
    list_display = ('url', 'user', 'valid_date', 'total_increase_price', 'status_verify', 'moderation', 'created',
                    'update')
    search_fields = ('url__url', )
    list_filter = ('url', 'status_verify', 'moderation', 'valid_date', 'created', 'update')
    readonly_fields = ('url', 'user', 'created', 'update', 'valid_date')
    list_select_related = ['user__user', 'url']
    save_on_top = True
    raw_id_fields = ['user', 'url']

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для уведомления пользователя"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        super(LinkAdmin, self).save_model(request, obj, form, change)
        obj.save(update_fields=update_fields)


admin.site.register(Link, LinkAdmin)
