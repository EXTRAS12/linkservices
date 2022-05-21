from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import DetailView, UpdateView

from .forms import UserRegisterForm, AuthenticationForm, ProfileForm
from .models import Profile
from .utils import send_email_for_verify
from django.contrib.auth.tokens import default_token_generator as token_generator


User = get_user_model()


class ProfileView(LoginRequiredMixin, DetailView):
    """Профиль"""
    model = Profile
    template_name = 'users/profile.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Редактирование профиля"""
    form_class = ProfileForm
    model = Profile
    template_name = 'users/edit_profile.html'
    success_url = '/profile/id={user_id}'

    def dispatch(self, request, *args, **kwargs):
        """ Пользователь может редактировать только свои сайты """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(ProfileUpdate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.instance.wmz)
        print(form.instance.ymoney)
        return super().form_invalid(form)


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class EmailVerify(View):
    """Подтверждения e-mail"""
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('profile')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


class Register(View):
    """Регистрация пользователя на сайте"""
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
