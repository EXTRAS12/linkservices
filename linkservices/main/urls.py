from django.urls import path

from .views import frontpage, HelpView, Catalog, Plugins


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('help/', HelpView.as_view(), name='help'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('plugins/', Plugins.as_view(), name='plugins'),

]
