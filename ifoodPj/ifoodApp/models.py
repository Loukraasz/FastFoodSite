from django.db import models
from .validators import validate_even

class Endereco(models.Model):
    id = models.AutoField(primary_key=id)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=40, validators=[validate_even])
    password = models.CharField(max_length=40)
    email = models.EmailField()
    sessionId = models.CharField(max_length=300, null=True, blank=True)
    phoneNumber = models.IntegerField(null=True)
    adress = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.username)
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    
    
class Pedido(models.Model):
    status_choices = (
        ("P", "Pedido realizado"),
        ("E", "Pedido entregue"),
        ("S", "Saiu p Entrega"),
        ("C", "Cancelado"),
        ("A", "Pedido em preparacao")
    )
    
    cliente = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    observacoes = models.CharField(max_length=300)
    valor = models.FloatField(null=True)
    status = models.CharField(max_length=1, choices=status_choices)
    
 
class Cart(models.Model):
    cliente = models.OneToOneField("User", on_delete=models.SET_NULL, null=True)
    total = models.FloatField(null=True)
    
class Info(models.Model):
    quantidade = models.IntegerField(null=True)
    produto = models.ForeignKey("Produto", on_delete=models.SET_NULL, null=True)
    carrinho = models.ForeignKey("Cart", on_delete=models.SET_NULL, null=True)
    total_p = models.FloatField(null=True)
    



    

    


   
