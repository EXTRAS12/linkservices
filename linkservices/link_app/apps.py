from django.apps import AppConfig


class LinkAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'link_app'
    verbose_name = 'Приложение ссылки'

    def ready(self):
        import link_app.signals