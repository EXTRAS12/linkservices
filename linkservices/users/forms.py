from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm as DjangoAuthenticationForm, )
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from users.utils import send_email_for_verify
from users.models import Profile

User = get_user_model()


class ProfileForm(forms.ModelForm):
    """Форма профиля"""

    class Meta:
        model = Profile
        fields = ('wmz', 'ymoney', 'user')


class AuthenticationForm(DjangoAuthenticationForm):
    captcha = CaptchaField(label='Введите капчу')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'].widget.attrs.update({'class': 'form-control',
                                                    'placeholder': 'Пожалуйста введите капчу'})

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'E-mail не верифицирован, проверьте вашу почту.',
                    code='invalid_login',
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введите капчу')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'].widget.attrs.update({'class': 'form-control',
                                                    'placeholder': 'Пожалуйста введите капчу'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'name_telegram', 'password1', 'password2')
