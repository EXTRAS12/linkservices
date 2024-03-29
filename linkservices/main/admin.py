from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from .models import *


class NewFlatpageInline(admin.StackedInline):
    """Для статических страниц"""
    model = NewFlatpage
    verbose_name = "Содержание"


class FlatPageNewAdmin(FlatPageAdmin):
    """Для статических страниц"""
    inlines = [NewFlatpageInline]
    fieldsets = (
        (None, {'fields': ('url', 'title', 'sites')}), (('Advanced options',), {
            'fields': ('template_name',),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')


class StatAdmin(admin.ModelAdmin):
    """Для статистики"""
    model = Stat
    list_display = ('balance_for_all_time', 'balance_current', 'balance_hold')


class HelpAdmin(admin.ModelAdmin):
    """Для раздела помощь"""
    model = Help


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)
admin.site.register(Plugin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Help, HelpAdmin)

admin.site.site_title = 'Вас приветствует linkservices.ru'
admin.site.site_header = 'Вас приветствует Linkservices.ru'
