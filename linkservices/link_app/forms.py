from django import forms
from .models import Link


class AddLinkForm(forms.ModelForm):
    """Форма добавления ссылки"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].widget.attrs.update({'class': 'form-control', 'rows': 4,
                                                 'placeholder': "Вставьте полноценный код "
                                                                "вашей ссылки с анкором или без"})

    class Meta:
        model = Link
        fields = ['url', 'user', 'link', 'count_month']


class ExtensionLinkForm(forms.ModelForm):
    """Продление ссылки"""

    class Meta:
        model = Link
        fields = ['url', 'user', 'count_month']


class UpdateLinkForm(forms.ModelForm):
    """Редактирование ссылки"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link2'].widget.attrs.update({'class': 'form-control', 'rows': 4,
                                                  'placeholder': "Вставьте полноценный код "
                                                                 "вашей ссылки с анкором или без"})

    class Meta:
        model = Link
        fields = ['url', 'user', 'link2']
