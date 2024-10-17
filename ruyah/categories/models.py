"""
Category Model

Model Fields:
- name: Category name
- description: Category description
- created_at: Date and time when the category was created
- updated_at: Date and time when the category was last updated

Model Properties:
- task_count: Number of tasks in the category
"""

from django.db import models


# Create your models here.
class Category(models.Model):
    """Task categories"""

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
    def task_count(self) -> int:
        """
        Number of tasks in the category

        Returns:
        int: Number of tasks in the category.
        """

        return self.tasks.count()

    def __str__(self) -> str:
        return self.name
