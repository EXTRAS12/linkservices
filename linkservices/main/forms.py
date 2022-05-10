from django import forms
from .models import WebSite


class AddSiteForm(forms.ModelForm):
    """Форма добавления сайтов"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Тематика не выбрана'

    class Meta:
        model = WebSite
        fields = ['url', 'category', 'price', 'yandex_stat', 'password_yandex']

