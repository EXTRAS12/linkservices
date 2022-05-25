from django.contrib import admin
from .models import Category, Status, WebSite
from link_app.models import Link


class LinkOrderAdmin(admin.TabularInline):
    model = Link
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    """Для категорий"""
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class StatusAdmin(admin.ModelAdmin):
    """Для статуса"""
    list_display = ('id', 'name')


class WebsiteAdmin(admin.ModelAdmin):
    """Сайты"""
    fields = ('url', 'user', 'category', 'status', 'price', 'total_link', 'yandex_x',
              'yandex_stat', 'password_yandex', 'created', 'update')
    list_display = ('url', 'category', 'status', 'price', 'user', 'total_link', 'yandex_x',
                    'created', 'update')
    search_fields = ('url', 'category', 'status')
    list_editable = ['status', ]
    list_filter = ('status', 'category', )
    readonly_fields = ('created', 'update')
    inlines = [LinkOrderAdmin]

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для уведомления пользователя"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        super(WebsiteAdmin, self).save_model(request, obj, form, change)
        obj.save(update_fields=update_fields)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(WebSite, WebsiteAdmin)

