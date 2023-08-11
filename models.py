""" Task models """


from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class List(models.Model):
    """Task Lists"""

    # The owner of the list
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Attributes
    name = models.CharField(max_length=32, db_index=True, help_text="List name")
    description = models.CharField(
        max_length=256, null=True, blank=True, help_text="Task list description"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta data"""

        ordering = ("id",)

    def __str__(self):
        return self.name


class Task(models.Model):
    """Tasks"""

    # The owner of the list
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # The list that the task belongs to
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    # Attributes
    title = models.CharField(max_length=32, db_index=True, help_text="Task title")
    description = models.CharField(
        max_length=256, null=True, blank=True, help_text="Task description"
    )
    completed = models.BooleanField(
        default=False, help_text="Designates if the task is completed"
    )
    starred = models.BooleanField(
        default=False, help_text="Designates if the task is important"
    )
    deadline = models.DateField(
        null=True, blank=True, db_index=True, help_text="Task deadline"
    )
    completion_rate = models.PositiveSmallIntegerField(
        default=0,
        help_text="Task completion percentage",
        validators=[
            validators.MaxValueValidator(
                100, "Ensure this value is less than or equal to 100."
            ),
            validators.MinValueValidator(
                0, "Ensure this value is greater than or equal to 0."
            ),
        ],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta data"""

        ordering = ("id",)
        constraints = [
            models.CheckConstraint(
                name="completion_rate_gte_0", check=models.Q(completion_rate__gte=0)
            ),
            models.CheckConstraint(
                name="completion_rate_lte_100", check=models.Q(completion_rate__lte=100)
            ),
        ]

    def __str__(self):
        return self.title
