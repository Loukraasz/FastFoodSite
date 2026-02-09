from django import forms
from .models import User, Endereco

class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = False
        
    class Meta:
        model = User
        fields = ["username","password","email","phoneNumber"]
        widgets = { 'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Numero de telefone'}),
}
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
        widgets = { 'rua': forms.TextInput(attrs={'placeholder': 'Digite o nome da rua'}),
            'numero': forms.NumberInput(attrs={'placeholder': 'Número'}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Complemento (opcional)'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade'})}   

        
 
