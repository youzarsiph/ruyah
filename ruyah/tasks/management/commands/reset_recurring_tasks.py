""" Command to set recurring tasks as incomplete.  """

from datetime import datetime
from typing import Union
from django.core.management.base import BaseCommand
from django.utils import timezone

from ruyah.tasks.models import Task


# Create your command here.
class Command(BaseCommand):
    """
    Command to set recurring tasks as incomplete.

    This management command identifies all recurring tasks that are marked as completed
    and sets their completion status to False. This is useful for managing tasks that
    need to be re-evaluated or re-assigned rather than creating new instances.

    The command checks for tasks that:
    - Are marked as recurring.
    - Have a start date that is less than or equal to the current time.
    - Currently marked as completed.

    Usage:
        To run this command, execute:
        python manage.py reset_recurring_tasks
    """

    help = "Set recurring tasks as incomplete."

    def handle(self, *args, **options) -> None:
        """
        The main entry point for the command execution.

        - Retrieves the current time to compare against task start dates.
        - Queries the database for recurring tasks that are marked as completed.
        - For each task found, updates its `is_completed` status to False and saves the change.

        Args:
            *args: Positional arguments passed to the command (not used).
            **options: Optional arguments passed to the command (not used).
        """

        now = timezone.now()

        # Get all ongoing recurring tasks that are completed
        recurring_tasks = Task.objects.filter(
            is_recurring=True,
            is_completed=True,  # Find completed tasks only
            recurrence_start_date__lte=now,
            # Ensure the task has not reached its end date
            recurrence_end_date__gte=now,  # Only include tasks that are still valid
        )

        for task in recurring_tasks:
            # Calculate the next occurrence based on recurrence_type and recurrence_interval
            next_occurrence = self.get_next_occurrence(task)

            if next_occurrence and next_occurrence > now:
                # Set the task's completion status to not completed
                task.is_completed = False
                task.save()  # Save the updated status to the database

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Task "{task.title}" has been marked as incomplete.'
                    )
                )

            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Task "{task.title}" has no valid next occurrence and will not be marked as incomplete.'
                    )
                )

    def get_next_occurrence(self, task) -> Union[datetime, None]:
        """
        Calculate the next occurrence of a recurring task based on its recurrence type and interval.

        Args:
            task (Task): The task object for which to calculate the next occurrence.

        Returns:
            datetime or None: The next occurrence date if valid, otherwise None.
        """

        match task.recurrence_type:
            case "daily":
                return task.recurrence_start_date + timezone.timedelta(
                    days=task.recurrence_interval
                )

            case "weekly":
                return task.recurrence_start_date + timezone.timedelta(
                    weeks=task.recurrence_interval
                )

            case "monthly":
                return task.recurrence_start_date + timezone.timedelta(
                    days=30 * task.recurrence_interval
                )  # Approximation

            case "yearly":
                return task.recurrence_start_date + timezone.timedelta(
                    days=365 * task.recurrence_interval
                )  # Approximation

            case _:
                return None
