from django.http import HttpResponse
from django.shortcuts import render
from .forms import EnderecoForm, NameForm
from .models import Produto, Pedido,User, Endereco,Cart

def index(request):
    if request.method == "GET":
        
        user = NameForm()
        endereco = EnderecoForm()
        '''
        e = Endereco(rua="132",complemento="op",bairro="sad",cidade="dsa",numero="12")
        e.save()
        u = User(username="fasasf", password="fas", email="gsd@gmail", phoneNumber="213", adress=e)
        u.save()
        produto = Produto(nome="pizza", descricao="pizza", valor="32.90")
        produto.save()
        pedido = Pedido(cliente=u,observacoes="nenhuma", valor="32.90", status="P")
        pedido.save()
        pedido.produto.add(produto)
        '''
        return render(request, "polls/index.html", {"user":user, "endereco":endereco})
    if request.method == "POST":
        user = NameForm(request.POST)
        endereco = EnderecoForm(request.POST)
        if user.is_valid() and endereco.is_valid():
            end_id = endereco.save()
            adress = user.save(commit=False)
            adress.adress_id = end_id.id
            adress.save()
            end_id.save()
            return HttpResponse("salvo")
        return HttpResponse("erro")


def cad(request):
    pizza = Produto.objects.get(nome="pizza")
    usuario = User.objects.get(username="lukas")
    pedido = Pedido(cliente=usuario,observacoes="nenhuma", valor="32.90", status="P")
    pedido.save()
    pedido.produto.add(pizza)
    return HttpResponse("nada por enquanto")

def pedido(request):
    if request.method == "GET":
        return render(request, "polls/pedido.html")
    usuario = User.objects.get(username="lukas")
    pizza = Produto.objects.filter(nome="pizza").values("valor")
    temaki = Produto.objects.filter(nome="temaki de salmao").values("valor")
    pizza_val = pizza[0]["valor"]
    temaki_val = temaki[0]["valor"]
    total = temaki_val + pizza_val
    pizza_obj = Produto.objects.get(nome="pizza")
    temaki_obj = Produto.objects.get(nome="temaki de salmao")
    carrinho = Cart(cliente=usuario,total=total)
    carrinho.save()
    carrinho.pedidos.add(temaki_obj,pizza_obj)
    
    
    
    return render(request, "polls/pedido.html")