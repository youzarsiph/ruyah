""" AppConf for tasks """


from django.apps import AppConfig


class TasksConfig(AppConfig):
    """App Configuration"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
