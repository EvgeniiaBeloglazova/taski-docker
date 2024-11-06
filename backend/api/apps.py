"""This class is responsible for managing the API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """This class is responsible for managing the API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
