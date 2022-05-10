from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import UserRegisterForm

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'name_telegram', 'email', 'date_joined', 'is_staff',  'email_verify')
    search_fields = ('username', 'email', 'date_joined', 'is_staff')
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
