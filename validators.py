""" Validators """


from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your validators here.
def validate_deadline(value: datetime) -> None:
    """Validate if the given deadline is after current datetime"""

    if value <= timezone.now():
        raise ValidationError(
            "The deadline should be set after the current date and time."
        )
