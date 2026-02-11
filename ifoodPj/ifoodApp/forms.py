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
        widgets = { 'username': forms.TextInput(attrs={'placeholder': 'Nome', 'autocomplete': 'off',"oninput":"cad()"}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha', 'autocomplete': 'off',"oninput":"passwordCheck()","onclick":"remove('pass_count','id_password','Senha')"}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'autocomplete': 'off',"oninput":"emailValidate()", "onclick":"remove('email','id_email','Email')"}),
            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Numero de telefone', 'autocomplete': 'off'}),
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
        widgets = { 'rua': forms.TextInput(attrs={'placeholder': 'Digite o nome da rua', 'autocomplete': 'off'}),
            'numero': forms.NumberInput(attrs={'placeholder': 'Número', 'autocomplete': 'off'}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Complemento (opcional)', 'autocomplete': 'off'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro', 'autocomplete': 'off'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade', 'autocomplete': 'off'})}   

        
 
