"""
Comment Model

Model Fields:
- user: Comment owner
- task: Commented task
- content: Comment content
- created_at: Date created
- updated_at: Last update
"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Comment(models.Model):
    """Task comments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Comments",
        help_text="Comment owner",
    )
    task = models.ForeignKey(
        "tasks.Task",
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Task",
    )
    content = models.CharField(
        max_length=512,
        db_index=True,
        help_text="Content",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.task}: {self.content[:10]}"
