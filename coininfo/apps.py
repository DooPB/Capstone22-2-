from django.apps import AppConfig


class CoininfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coininfo'
    def ready(self):
        from .cron import main
        main()
