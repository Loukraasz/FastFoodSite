from django.http import HttpResponse
from django.shortcuts import render
from .forms import EnderecoForm, NameForm
from .models import Produto, Pedido,User, Endereco

def index(request):
    user = NameForm()
    endereco = EnderecoForm()
    e = Endereco(rua="132",complemento="op",bairro="sad",cidade="dsa",numero="12")
    e.save()
    u = User(username="fasasf", password="fas", email="gsd@gmail", phoneNumber="213", adress=e)
    u.save()
    produto = Produto(nome="pizza", descricao="pizza", valor="32.90")
    produto.save()
    pedido = Pedido(cliente=u,observacoes="nenhuma", valor="32.90", status="P")
    pedido.save()
    pedido.produto.add(produto)
    
   
    
    
    return render(request, "polls/index.html", {"user":user, "endereco":endereco})
def cad(request):
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