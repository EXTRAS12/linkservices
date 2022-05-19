from django import forms

from users.models import Profile


class ProfileForm(forms.ModelForm):
    """Форма профиля"""

    class Meta:
        model = Profile
        fields = (
            'wmz',
            'ymoney',
            'user',
            )
