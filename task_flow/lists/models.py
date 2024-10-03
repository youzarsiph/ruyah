"""
List Model

Model Fields:
- user: List owner
- name: List name
- description: List description
- created_at: Date created
- updated_at: Last update

Model Properties:
- progress: Calculate the progress of the task list
- task_count: Calculate the number of tasks in the task list
"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class List(models.Model):
    """Task lists"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lists",
        help_text="Task list owner",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    @property
    def progress(self) -> float:
        """
        Task list progress.

        Returns:
        float: The progress of the task list.
        """

        return (
            self.tasks.filter(is_completed=True).count() / self.tasks.count()
            if self.tasks.count() != 0
            else 0
        )

    @property
    def task_count(self) -> int:
        """
        Number of tasks in the task list.

        Returns:
        int: The number of tasks in the task list.
        """

        return self.tasks.count()

    def __str__(self) -> str:
        return self.name
