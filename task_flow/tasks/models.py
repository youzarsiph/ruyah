"""
Task Model

Model Fields:
- user: Task owner
- list: Task list
- title: Task title
- description: Task description
- is_completed: Task completion status
- is_starred: Task importance status
- deadline: Task deadline
- priority: Task priority
- tags: Task tags
- progress: Task progress
- created_at: Task creation date
- updated_at: Task last update date
"""

from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
from task_flow.tasks.validators import validate_deadline
from task_flow.tasks import TASK_PRIORITIES


# Create your models here.
User = get_user_model()


class Task(models.Model):
    """Tasks"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Owner",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Task category",
    )
    list = models.ForeignKey(
        "lists.List",
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Task list",
    )
    title = models.CharField(
        max_length=32,
        db_index=True,
        help_text="Title",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
    )
    attachment = models.FileField(
        null=True,
        blank=True,
        upload_to="files/tasks/",
        help_text="Attach a file",
    )
    is_completed = models.BooleanField(
        default=False,
        help_text="Designates if the task is completed",
    )
    is_starred = models.BooleanField(
        default=False,
        help_text="Designates if the task is added to favorites",
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Task deadline",
        validators=[validate_deadline],
    )
    priority = models.PositiveSmallIntegerField(
        default=0,
        help_text="Priority",
        choices=TASK_PRIORITIES,
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        related_name="tasks",
        help_text="Task tags",
    )
    progress = models.PositiveSmallIntegerField(
        default=0,
        help_text="Task progress",
        validators=[
            validators.MaxValueValidator(
                100,
                "Ensure this value is less than or equal to 100",
            ),
            validators.MinValueValidator(
                0,
                "Ensure this value is greater than or equal to 0",
            ),
        ],
    )
    sub_tasks = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="subtasks",
        help_text="Subtasks",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    class Meta:
        """Meta Data"""

        constraints = [
            models.CheckConstraint(
                name="progress_gte_0",
                check=models.Q(progress__gte=0),
            ),
            models.CheckConstraint(
                name="progress_lte_100",
                check=models.Q(progress__lte=100),
            ),
        ]

    def __str__(self) -> str:
        return self.title
