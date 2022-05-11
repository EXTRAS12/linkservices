from django.urls import path

from .views import FrontPage, Profile, Help, Catalog, Plugins


urlpatterns = [
    path('', FrontPage.as_view(), name='frontpage'),
    path('profile/', Profile.as_view(), name='profile'),
    path('help/', Help.as_view(), name='help'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('plugins/', Plugins.as_view(), name='plugins'),

]
