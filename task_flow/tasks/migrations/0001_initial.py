# Generated by Django 5.1 on 2024-10-05 08:07

import django.core.validators
import django.db.models.deletion
import task_flow.tasks.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        ("lists", "0001_initial"),
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(db_index=True, help_text="Title", max_length=32),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, help_text="Description", max_length=256
                    ),
                ),
                (
                    "attachment",
                    models.FileField(
                        blank=True,
                        help_text="Attach a file",
                        null=True,
                        upload_to="files/tasks/",
                    ),
                ),
                (
                    "is_completed",
                    models.BooleanField(
                        default=False, help_text="Designates if the task is completed"
                    ),
                ),
                (
                    "is_starred",
                    models.BooleanField(
                        default=False,
                        help_text="Designates if the task is added to favorites",
                    ),
                ),
                (
                    "deadline",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        help_text="Task deadline",
                        null=True,
                        validators=[task_flow.tasks.validators.validate_deadline],
                    ),
                ),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (
                                0,
                                "Critical (Urgent and Important): Tasks that must be completed immediately and have significant consequences if not done.",
                            ),
                            (
                                1,
                                "High Priority (Important but Not Urgent): Important tasks that should be handled soon but can be scheduled for later. They contribute to long-term goals.",
                            ),
                            (
                                2,
                                "Medium Priority (Urgent but Not Important): Tasks that need to be done soon but are not as crucial. These may serve as interruptions but should still be addressed promptly.",
                            ),
                            (
                                3,
                                "Low Priority (Not Urgent, Not Important): Tasks that have little impact on overall goals and can be postponed or delegated.",
                            ),
                            (
                                4,
                                "Delegate: Tasks that can be passed on to someone else. It may be important, but the person assigning it prefers others to handle it.",
                            ),
                            (
                                5,
                                "Someday/Maybe: Tasks that are not immediate priorities but could become relevant in the future. Good for brainstorming or potential future projects.",
                            ),
                        ],
                        default=0,
                        help_text="Priority",
                    ),
                ),
                (
                    "progress",
                    models.PositiveSmallIntegerField(
                        default=0,
                        help_text="Task progress",
                        validators=[
                            django.core.validators.MaxValueValidator(
                                100, "Ensure this value is less than or equal to 100"
                            ),
                            django.core.validators.MinValueValidator(
                                0, "Ensure this value is greater than or equal to 0"
                            ),
                        ],
                    ),
                ),
                (
                    "is_recurring",
                    models.BooleanField(
                        default=False, help_text="Designates if the task is recurring"
                    ),
                ),
                (
                    "recurrence_type",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (0, "Daily"),
                            (1, "Weekly"),
                            (2, "Monthly"),
                            (3, "Yearly"),
                            (4, "Custom"),
                        ],
                        help_text="The type of recurrence",
                        null=True,
                    ),
                ),
                (
                    "recurrence_interval",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Interval of recurrence (e.g., every 2 days)",
                    ),
                ),
                (
                    "recurrence_start_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date when the recurrence starts",
                        null=True,
                    ),
                ),
                (
                    "recurrence_end_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date when the recurrence ends (optional)",
                        null=True,
                    ),
                ),
                (
                    "occurrence_count",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Number of occurrences before stopping (optional)",
                        null=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Task category",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="categories.category",
                    ),
                ),
                (
                    "list",
                    models.ForeignKey(
                        help_text="Task list",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="lists.list",
                    ),
                ),
                (
                    "sub_tasks",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Subtasks",
                        related_name="subtasks",
                        to="tasks.task",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Task tags",
                        related_name="tasks",
                        to="tags.tag",
                    ),
                ),
            ],
        ),
    ]
