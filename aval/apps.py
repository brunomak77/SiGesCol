from django.apps import AppConfig


class AvalConfig(AppConfig):
    name = 'aval'
    verbose_name = 'Avaliação'

    def ready(self):
        import aval.signals
