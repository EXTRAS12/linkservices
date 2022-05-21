from django import forms
from .models import WebSite


class AddSiteForm(forms.ModelForm):
    """Форма добавления сайтов"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Тематика не выбрана'
        self.fields['category'].widget.attrs.update({'class': 'form-control select2', 'readonly': 'readonly'})
        self.fields['url'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['yandex_stat'].widget.attrs.update({'class': 'form-control'})
        self.fields['yandex_x'].widget.attrs.update({'class': 'form-control'})
        self.fields['password_yandex'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = WebSite
        fields = ['url', 'category', 'price', 'total_link', 'yandex_stat', 'yandex_x',
                  'password_yandex']
