from django.core.exceptions import ValidationError


def validate_even(value):
    print("S")
    if not isinstance(value, str):
        print("A")
        raise ValueError("paia")
    if value == "caralho":
        print("R")
        raise ValidationError("sad")

        