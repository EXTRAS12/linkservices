from django.contrib import admin
from .models import Category, Status, WebSite


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
    fields = ('url', 'category', 'status', 'price', 'total_link', 'sold_link', 'yandex_x',
              'yandex_stat', 'password_yandex', 'created', 'update')
    list_display = ('url', 'category', 'status', 'total_link', 'sold_link', 'yandex_x',
                    'created', 'update')
    search_fields = ('url', 'category', 'status')
    # list_editable = ('status',)
    list_filter = ('status', 'category', )
    readonly_fields = ('created', 'update')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(WebSite, WebsiteAdmin)
