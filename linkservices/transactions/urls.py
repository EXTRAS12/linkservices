from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, CancelWithdraw


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path('cancel/<int:pk>/', CancelWithdraw.as_view(), name='cancel-withdraw'),
]
