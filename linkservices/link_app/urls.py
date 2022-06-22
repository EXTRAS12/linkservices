from .views import *
from django.urls import path


urlpatterns = [
    path('', MyLinks.as_view(), name='my-links'),
    path('catalog/buy_link/<int:pk>/', BuyLink.as_view(), name='buy-link'),
    path('extension_link/<int:pk>/', ExtensionLink.as_view(), name='extension-link'),
    path('update_link/<int:pk>/', UpdateLink.as_view(), name='update-link'),

]
