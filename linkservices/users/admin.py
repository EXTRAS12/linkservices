from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.forms import UserRegisterForm
from .models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'name_telegram', 'email', 'date_joined', 'is_staff',  'email_verify')
    search_fields = ('username', 'email', 'date_joined', 'is_staff')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "email_verify",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username",  "email", "password1", "password2"),
            },
        ),
    )
    add_form = UserRegisterForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профили пользователей"""
    list_display = ('user', 'current_balance', 'hold_balance', 'output_balance', 'chat_id', 'TOKEN',
                    'created', 'update')

