from django import forms
from .models import User

class nameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","email","phoneNumber"]
        
