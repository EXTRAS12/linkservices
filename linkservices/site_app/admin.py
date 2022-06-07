from django.contrib import admin
from .models import Category, WebSite
from link_app.models import Link


# class LinkOrderAdmin(admin.TabularInline):
#     """Возможность добавлять и изменять ссылки внутри сайта в админке"""
#     model = Link
#     raw_id_fields = ['user', 'url']
#     extra = 1


class CategoryAdmin(admin.ModelAdmin):
    """Для категорий"""
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class WebsiteAdmin(admin.ModelAdmin):
    """Сайты"""
    fields = ('url', 'user', 'category', 'status', 'price', 'increase', 'total_link', 'yandex_x',
              'yandex_stat', 'password_yandex', 'created', 'update')
    list_display = ('url', 'category', 'status', 'price', 'get_increase_price', 'user', 'increase', 'total_link', 'yandex_x',
                    'created', 'update')
    search_fields = ('url',)
    list_filter = ('status', 'category', )
    readonly_fields = ('url', 'user', 'created', 'update')
    list_select_related = ['user__user', 'category']
    save_on_top = True

    # inlines = [LinkOrderAdmin]

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для уведомления пользователя"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        super(WebsiteAdmin, self).save_model(request, obj, form, change)
        obj.save(update_fields=update_fields)


admin.site.register(Category, CategoryAdmin)
admin.site.register(WebSite, WebsiteAdmin)
