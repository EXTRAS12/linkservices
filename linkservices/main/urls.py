from django.urls import path

from .views import FrontPage, Profile, MySites, add_site, MyLinks, BuyLink, Help, Catalog, Plugins


urlpatterns = [
    path('', FrontPage.as_view(), name='frontpage'),
    path('profile/', Profile.as_view(), name='profile'),
    path('mysites/', MySites.as_view(), name='my-sites'),
    path('mysites/addsite/', add_site, name='add-site'),
    path('mylinks/', MyLinks.as_view(), name='my-links'),
    path('catalog/buy_link/<int:pk>/', BuyLink.as_view(), name='buy-link'),
    path('help/', Help.as_view(), name='help'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('plugins/', Plugins.as_view(), name='plugins'),

]
