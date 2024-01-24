""" Task Data Models """


from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
from tasks.validators import validate_deadline


# Create your models here.
User = get_user_model()


class List(models.Model):
    """Task Lists"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lists",
        help_text="Task list owner",
    )
    name = models.CharField(
        max_length=32,
        db_index=True,
        help_text="Task list name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Task list description",
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
        """Returns completion"""

        return self.tasks.filter(is_completed=True).count() / self.tasks.count()

    @property
    def task_count(self) -> float:
        """Returns number of tasks in the list"""

        return self.tasks.count()

    def __str__(self):
        return self.name


class Task(models.Model):
    """Tasks"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Task owner",
    )
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Task list",
    )
    title = models.CharField(
        max_length=32,
        db_index=True,
        help_text="Task title",
    )
    description = models.CharField(
        max_length=256,
        help_text="Task description",
    )
    is_completed = models.BooleanField(
        default=False,
        help_text="Designates if the task is completed",
    )
    is_starred = models.BooleanField(
        default=False,
        help_text="Designates if the task is important",
    )
    deadline = models.DateTimeField(
        db_index=True,
        null=True,
        blank=True,
        help_text="Task deadline",
        validators=[validate_deadline],
    )
    progress = models.PositiveSmallIntegerField(
        default=0,
        help_text="Task completion progress",
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
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

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

    def __str__(self):
        return self.title
