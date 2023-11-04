from django.db import models
from .validators import validate_even

class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)

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
    valor = models.FloatField()
    status = models.CharField(max_length=1, choices=status_choices)
    produto = models.ManyToManyField(Produto)

class User(models.Model):
    username = models.CharField(max_length=40, validators=[validate_even])
    password = models.CharField(max_length=40)
    email = models.EmailField()
    phoneNumber = models.IntegerField(null=True)
    adress = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.username)
    

    


   
