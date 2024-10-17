"""
User Model

Model Fields:
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Users"""

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/users/",
        help_text="User profile image",
    )

    @property
    def task_count(self) -> int:
        """
        Number of tasks in the task list.

        Returns:
        int: The number of tasks in the task list.
        """

        return self.tasks.count()
