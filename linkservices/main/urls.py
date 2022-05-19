from django.urls import path

from .views import FrontPage, ProfileView, Help, Catalog, Plugins, ProfileUpdate

urlpatterns = [
    path('', FrontPage.as_view(), name='frontpage'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path("edit/<int:pk>", ProfileUpdate.as_view(), name="edit_profile"),
    path('help/', Help.as_view(), name='help'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('plugins/', Plugins.as_view(), name='plugins'),

]
