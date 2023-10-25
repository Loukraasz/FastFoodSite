from django.core.exceptions import ValidationError

def validate_even(value):
    if not isinstance(value, str):
        raise ValueError("paia")
    if value =="teste":
        raise ValidationError("sad")

        