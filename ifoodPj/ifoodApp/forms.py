from django import forms
from .models import User, Endereco

class nameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False
        
    class Meta:
        model = User
        fields = ["username","password","email","phoneNumber"]
        required = ["username","password","email","phoneNumber"]
class EnderecoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False
        
    class Meta:
        model = Endereco
        fields = ["rua","numero","complemento","cidade","bairro"]
        required = ["rua","numero","complemento","cidade","bairro"]

        
 
