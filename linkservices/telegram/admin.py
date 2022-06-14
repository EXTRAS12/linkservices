from dataclasses import fields
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Рассылка"""
    class Meta:
        model = Event
        fields = '__all__'
