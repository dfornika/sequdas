from django.apps import AppConfig

class SequdasConfig(AppConfig):
    name = 'sequdas'
    
    def ready(self):
        from . import signals
