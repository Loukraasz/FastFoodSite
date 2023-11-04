from django.core.exceptions import ValidationError


def validate_even(value):
    if not isinstance(value, str):
        raise ValueError("not is instance")
    if value == "":
        raise ValidationError("validation")

        