from django.apps import AppConfig


class DOProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'd_o_profile'

    def ready(self):
        import d_o_profile.signals
