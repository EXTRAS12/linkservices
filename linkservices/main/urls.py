from django.urls import path

from .views import FrontPage, Help, Catalog, Plugins


urlpatterns = [
    path('', FrontPage.as_view(), name='frontpage'),
    path('help/', Help.as_view(), name='help'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('plugins/', Plugins.as_view(), name='plugins'),

]
