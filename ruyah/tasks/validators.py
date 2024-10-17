""" Validators for tasks """

from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_deadline(value: datetime) -> None:
    """
    Validate if the given deadline is greater than or equal to the current datetime.

    Parameters:
    value (datetime): The deadline to validate.

    Raises:
    ValidationError: If the deadline is less than the current datetime.
    """

    if value <= timezone.now():
        raise ValidationError(
            f"The deadline {value} is not valid."
            "It should be set after the current date and time."
        )
