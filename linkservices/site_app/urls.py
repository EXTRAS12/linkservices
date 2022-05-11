from .views import MySites, add_site, UpdateSite, DeleteSite
from django.urls import path


urlpatterns = [
    path('', MySites.as_view(), name='my-sites'),
    path('add-site/', add_site, name='add-site'),
    path('<int:pk>/update/', UpdateSite.as_view(), name='update-site'),
    path('<int:pk>/delete/', DeleteSite.as_view(), name='delete-site'),

]
