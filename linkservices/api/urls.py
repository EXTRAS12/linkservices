from .views import SiteApiView, LinkApiView
from django.urls import path


urlpatterns = [
    path('sitelist/', SiteApiView.as_view(), name='site-api'),
    path('linklist/', LinkApiView.as_view(), name='link-api'),
 ]
