from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', include('main.urls')),
    path('', include('users.urls')),
    path('my-sites/', include('site_app.urls')),
    path('my-links/', include('link_app.urls')),
    path('telega/', include('telegram.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
