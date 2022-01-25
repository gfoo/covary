from django.apps import AppConfig


class FakeProbeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_probe'
