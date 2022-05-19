from django import forms
from .models import Link


class AddLinkForm(forms.ModelForm):
    """Форма добавления сайтов"""

    class Meta:
        model = Link
        fields = ['url', 'user_email', 'link', 'count_month', 'price_per_item']
