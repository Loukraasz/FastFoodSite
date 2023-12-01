from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from ifoodApp import send_email
from .forms import EnderecoForm, NameForm
from .models import Produto, User ,Cart

def index(request):
    if request.method == "GET":
        global sessionUser
        request.session['session'] = "sessions"
        sessionUser = request.COOKIES.get("sessionid")
        return render(request, "polls/index.html",)
    email_login = request.POST.get("lEmail")
    password_login = request.POST.get("lPassword")
    users_email = User.objects.filter(email=email_login).first()
    users = User.objects.filter(username=email_login).first()
    if users_email or users:
        user = User.objects.get(username=email_login)
        password_user = user.password
        if password_user == password_login:
            sessionUser
            user.sessionId = sessionUser
            user.save()
            return render(request, "polls/platform.html")
        else:
            return HttpResponse("asd")
    return HttpResponse("paia")
        

def cad(request):
    if request.method == "GET":
        user = NameForm()
        endereco = EnderecoForm()
        return render(request, "polls/cad.html", {"user": user, "endereco":endereco})
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


def rec_password(request):
    if request.method == "GET":
        return render(request, "polls/rec_password.html")
    email = request.POST.get("rec_email")
    try:
        email_user = User.objects.get(email=email)
        send_email.send_emails(email_user.email)
        return render(request, "polls/confirm_email.html")
    except ObjectDoesNotExist:
        return HttpResponse("erro")
    
def confirm_email(request):
    if request.method == "GET":
        return render(request, "polls/confirm_email.html")
    code = request.POST.get("rec_code")
    if code == send_email.final:
        return HttpResponse("bala")
    return HttpResponse("erro")
        
    
def pedido(request):
    if request.method == "GET":
        return render(request, "polls/pedido.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    usuario_id = usuario.id
    cart = Cart.objects.get(cliente_id = usuario_id)
    cart.delete()
    return render(request, "polls/pedido.html")


def platform(request):
    if request.method == "GET":
        relogin = "para continuar faca o login novamente"
        relog = {"relogin":relogin}
        userP = request.COOKIES.get("sessionid")
        try:
            logUser = User.objects.get(sessionId=userP)
            return render(request, "polls/platform.html")
        except ObjectDoesNotExist:
            
            return render(request, "polls/login.html", relog)
    else:
        userP = request.COOKIES.get("sessionid")
        try:
            logUser = User.objects.get(sessionId=userP)
            logUser.sessionId = None
            logUser.save()
        except ObjectDoesNotExist:
            return render(request, "polls/login.html", relog)
        return render(request, "polls/login.html")

def pizza(request):
    if request.method == "GET":
        return render(request, "polls/pizza.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    pizza = Produto.objects.filter(nome="pizza").values("valor")
    pizza_val = pizza[0]["valor"]
    pizza_obj = Produto.objects.get(nome="pizza")
    if cart:
        cart.total += pizza_val
        cart.pedidos.add(pizza_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/pedido.html")


def temaki_salmao(request):
    if request.method == "GET":
        return render(request, "polls/temaki_salmao.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
    temaki_salmao_val = temaki_salmao[0]["valor"]
    temaki_obj = Produto.objects.get(nome="temaki de salmao")
    if cart:
        cart.total += temaki_salmao_val
        cart.pedidos.add(temaki_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/temaki_salmao.html")

def esfiha(request):
    if request.method == "GET":
        return render(request, "polls/esfiha.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    esfiha = Produto.objects.filter(nome="esfiha").values("valor")
    esfiha_val = esfiha[0]["valor"]
    esfiha_obj = Produto.objects.get(nome="esfiha")
    if cart:
        cart.total += esfiha_val
        cart.pedidos.add(esfiha_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/esfiha.html")


def sorvete(request):
    if request.method == "GET":
        return render(request, "polls/sorvete.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    sorvete = Produto.objects.filter(nome="sorvete").values("valor")
    sorvete_val = sorvete[0]["valor"]
    sorvete_obj = Produto.objects.get(nome="sorvete")
    if cart:
        cart.total += sorvete_val
        cart.pedidos.add(sorvete_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/sorvete.html")


def bolo(request):
    if request.method == "GET":
        return render(request, "polls/bolo.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    bolo = Produto.objects.filter(nome="bolo").values("valor")
    bolo_val = bolo[0]["valor"]
    bolo_obj = Produto.objects.get(nome="bolo")
    if cart:
        cart.total += bolo_val
        cart.pedidos.add(bolo_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/bolo.html")


def coca_cola(request):
    if request.method == "GET":
        return render(request, "polls/coca_cola.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    cart = Cart.objects.get(cliente_id=usuario.id)
    coca_cola = Produto.objects.filter(nome="temaki de salmao").values("valor")
    coca_cola_val = coca_cola[0]["valor"]
    coca_cola_obj = Produto.objects.get(nome="temaki de salmao")
    if cart:
        cart.total += coca_cola_val
        print(cart.total)
        cart.pedidos.add(coca_cola_obj)
        cart.save()
        return render(request, "polls/pedido.html")
    return render(request, "polls/coca_cola.html")


    