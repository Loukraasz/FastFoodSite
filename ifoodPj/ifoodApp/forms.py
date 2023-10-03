from django.forms import ModelForm
from ifoodApp.models import User

class nameForm(ModelForm):
    class meta:
        model = User
        fields = ["username","password","email","phoneNumber"]
        
form = nameForm()

article = User.objects.get(pk=1)
form = nameForm(instance=article)