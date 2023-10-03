from django.forms import ModelForm
from .models import User

class nameForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password","email","phoneNumber"]
        
