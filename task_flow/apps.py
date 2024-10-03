""" AppConf for tasks """

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """App Configuration for tasks"""

    name = "task_flow"
    default_auto_field = "django.db.models.BigAutoField"
