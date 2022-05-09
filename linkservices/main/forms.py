from django import forms
from .models import WebSite


class AddSiteForm(forms.ModelForm):
    """Форма добавления сайтов"""

    class Meta:
        model = WebSite
        fields = ['url', 'category', 'price', 'yandex_stat', 'password_yandex']

