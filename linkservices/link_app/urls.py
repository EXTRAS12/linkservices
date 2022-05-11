from .views import *
from django.urls import path


urlpatterns = [
    path('my-links/', MyLinks.as_view(), name='my-links'),
    path('catalog/buy_link/<int:pk>/', BuyLink.as_view(), name='buy-link'),

]
