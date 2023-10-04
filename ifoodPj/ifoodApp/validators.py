from django.core.exceptions import ValidationError

def validate_even(value):
    if not isinstance(value, str):
        print("porra")
        raise ValueError("paia")
    if value =="":
        print("cu")
        raise ValidationError("ai nao funfou")