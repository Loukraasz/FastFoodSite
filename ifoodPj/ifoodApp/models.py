from django.db import models
from .validators import validate_even

class User(models.Model):
    username = models.CharField(max_length=40, validators=[validate_even])
    password = models.CharField(max_length=40)
    email = models.EmailField()
    phoneNumber = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.username)
