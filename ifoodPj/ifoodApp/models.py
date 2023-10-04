from typing import Any
from django.db import models
from .validators import validate_even

class User(models.Model):
    username = models.CharField(max_length=40, blank=True, validators=[validate_even])
    password = models.CharField(max_length=40, blank=True, validators=[validate_even])
    email = models.EmailField(blank=True, validators=[validate_even])
    phoneNumber = models.IntegerField(null=True, blank=True, validators=[validate_even])
    
    def __str__(self):
        return str(self.username)
