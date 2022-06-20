from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


from .views import Register, EmailVerify, MyLoginView, ProfileView, ProfileUpdate


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),

    path('', include('django.contrib.auth.urls')),

    path('invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),

    path('verify_email/<uidb64>/<token>', EmailVerify.as_view(), name='verify_email'),

    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('register/', Register.as_view(), name='register'),
    path('profile/id=<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit/id=<int:pk>', ProfileUpdate.as_view(), name='edit_profile'),
]
