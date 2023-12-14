from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from ifoodApp import send_email
from .forms import EnderecoForm, NameForm
from .models import Pedido, Produto, User ,Cart

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
            session = request.COOKIES.get("sessionid")
            user.sessionId = session
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
        global email_user
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
        return render(request, "polls/password_change.html")
    return HttpResponse("erro")

def password_change(request):
    if request.method == "GET":
        return render(request, "polls/password_change.html")
    np = request.POST.get("new_pass")
    npc = request.POST.get("new_pass_conf")
    if np == npc:
        email_user.password = npc
        email_user.save()
        return render(request, "polls/index.html")
    else:
        return HttpResponse("paia")
        
    
def pedido(request):
    if request.method == "GET":
        session = request.COOKIES.get("sessionid")
        userC = User.objects.get(sessionId = session)
        if userC:
            cart = Cart.objects.get(cliente_id = userC.id)
            if cart:
                return render(request, "polls/pedido.html")
        return render(request, "polls/pedido.html")
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    usuario_id = usuario.id
    cart = Cart.objects.get(cliente_id = usuario_id)
    print(cart)
    pedido = Pedido(observacoes="", valor=cart.total,status ="P" , cliente_id = usuario_id)
    products = cart.produto.all().values("nome")
    products_val = cart.produto.all().values("valor")
    all_products = products.count()
    counterP = 0
    counterV = 0
    list_product = []
    list_productV = []
    while counterP < all_products:
        product = products[counterP]["nome"]
        print(product)
        list_product.append(product)
        counterP += 1
    while counterV < all_products:
        productV = products_val[counterV]["valor"]
        print(productV)
        list_productV.append(productV)
        counterV += 1
    print(list_productV, list_product)
    pedido.save()
    return render(request, "polls/pedido.html")


def platform(request):
    if request.method == "GET":
        relogin = "para continuar faca o login novamente"
        relog = {"relogin":relogin}
        userP = request.COOKIES.get("sessionid")
        try:
            logUser = User.objects.get(sessionId=userP)
            if logUser.sessionId == None:
                request.session['session'] = "sessions"
                global session
                session = request.COOKIES.get("sessionid")
                return render(request, "polls/index.html", relog)
            return render(request, "polls/platform.html")
        except ObjectDoesNotExist:
            return render(request, "polls/index.html", relog)
    else:
        userP = request.COOKIES.get("sessionid")
        logUser = User.objects.get(sessionId=userP)
        logUser.sessionId = None
        logUser.save()
        return render(request, "polls/index.html")

def pizza(request):
    if request.method == "GET":
        pizza = Produto.objects.filter(nome="pizza").values("valor")
        pizza_val = pizza[0]["valor"]
        return render(request, "polls/pizza.html", {"product":pizza_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        pizza = Produto.objects.filter(nome="pizza").values("valor")
        pizza_obj = Produto.objects.get(nome="pizza")
        pizza_val_cart = request.POST.get("total_cart")
        pizza_val_format = float(pizza_val_cart)
        cart_a = Cart(total=pizza_val_format, cliente_id=usuario.id)
        cart_a.save()
        cart_a.produto.add(pizza_obj)
        return redirect("pedido")
    pizza = Produto.objects.filter(nome="pizza").values("valor")
    print(pizza)
    pizza_val = pizza[0]["valor"]
    pizza_obj = Produto.objects.get(nome="pizza")
    pizza_val_cart = request.POST.get("total_cart")
    pizza_val_format = float(pizza_val_cart)
    if cart:
        cart.total += pizza_val_format 
        cart.produto.add(pizza_obj)
        cart.save()
        return redirect("pedido")
    return redirect("pedido")


def temaki_salmao(request):
    if request.method == "GET":
        temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
        temaki_salmao_val = temaki_salmao[0]["valor"]
        return render(request, "polls/temaki_salmao.html", {"product":temaki_salmao_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
        temaki_salmao_val = temaki_salmao[0]["valor"]
        temaki_obj = Produto.objects.get(nome="temaki de salmao")
        temaki_cart = request.POST.get("total_cart")
        temaki_format = float(temaki_cart)
        cart_a = Cart(total=temaki_salmao_val, cliente_id=usuario.id)
        cart_a.produto.add(temaki_obj)
        cart_a.save()
        return redirect("pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
    temaki_obj = Produto.objects.get(nome="temaki de salmao")
    temaki_cart = request.POST.get("total_cart")
    temaki_format = float(temaki_cart)
    if cart:
        cart.total += temaki_format
        cart.produto.add(temaki_obj)
        cart.save()
        return redirect("pedido")
    return redirect("pedido")

def esfiha(request):
    if request.method == "GET":
        esfiha = Produto.objects.filter(nome="esfiha").values("valor")
        esfiha_val = esfiha[0]["valor"]
        return render(request, "polls/esfiha.html", {"product":esfiha_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        esfiha = Produto.objects.filter(nome="esfiha").values("valor")  
        esfiha_obj = Produto.objects.get(nome="esfiha")
        esfiha_cart = request.POST.get("total_cart")
        esfiha_format = float(esfiha_cart)
        cart_a = Cart(total=esfiha_format, cliente_id=usuario.id)
        cart_a.produto.add(esfiha_obj)
        cart_a.save()
        return redirect("pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    esfiha = Produto.objects.filter(nome="esfiha").values("valor")
    esfiha_obj = Produto.objects.get(nome="esfiha")
    esfiha_cart = request.POST.get("total_cart")
    esfiha_format = float(esfiha_cart)
    if cart:
        cart.total += esfiha_format
        cart.produto.add(esfiha_obj)
        cart.save()
        return redirect("pedido")
    return redirect("pedido")


def sorvete(request):
    if request.method == "GET":
        sorvete = Produto.objects.filter(nome="sorvete").values("valor")
        sorvete_val = sorvete[0]["valor"]
        return render(request, "polls/sorvete.html", {"product":sorvete_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        sorvete = Produto.objects.filter(nome="sorvete").values("valor")
        sorvete_obj = Produto.objects.get(nome="sorvete")
        sorvete_cart = request.POST.get("total_cart")
        sorvete_format = float(sorvete_cart)
        cart_a = Cart(total=sorvete_format, cliente_id=usuario.id)
        cart_a.produto.add(sorvete_obj)
        cart_a.save()
        return redirect("pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    sorvete = Produto.objects.filter(nome="sorvete").values("valor")
    sorvete_val = sorvete[0]["valor"]
    sorvete_obj = Produto.objects.get(nome="sorvete")
    sorvete_cart = request.POST.get("total_cart")
    sorvete_format = float(sorvete_format)
    if cart:
        cart.total += sorvete_format
        cart.produto.add(sorvete_obj)
        cart.save()
        return redirect("pedido")
    return redirect("pedido")


def bolo(request):
    if request.method == "GET":
        bolo = Produto.objects.filter(nome="bolo").values("valor")
        bolo_val = bolo[0]["valor"]
        return render(request, "polls/bolo.html", {"product":bolo_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        bolo = Produto.objects.filter(nome="bolo").values("valor")     
        bolo_obj = Produto.objects.get(nome="bolo")
        bolo_cart = request.POST.get("total_cart")
        bolo_format = float(bolo_cart)
        cart_a = Cart(total=bolo_format, cliente_id=usuario.id)
        cart.produto.add(bolo_obj)
        cart_a.save()
        return redirect("pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    bolo = Produto.objects.filter(nome="bolo").values("valor")
    bolo_val = bolo[0]["valor"]
    bolo_obj = Produto.objects.get(nome="bolo")
    bolo_cart = request.POST.get("total_cart")
    bolo_format = float(bolo_cart)
    if cart:
        cart.total += bolo_format
        cart_a.produto.add()
        cart.save()
        return redirect("pedido")
    return redirect("pedido")


def coca_cola(request):
    if request.method == "GET":
        coca_cola = Produto.objects.filter(nome="coca cola").values("valor")
        coca_cola_val = coca_cola[0]["valor"]
        return render(request, "polls/coca_cola.html", {"product":coca_cola_val})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    try:
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        coca_cola = Produto.objects.filter(nome="coca cola").values("valor")
        coca_cola_obj = Produto.objects.get(nome="coca cola")
        coca_cola_cart = request.POST.get("total_cart")
        coca_cola_format = float(coca_cola_cart)
        cart_a = Cart(total=coca_cola_format, cliente_id=usuario.id)
        cart_a.produto.add(coca_cola_obj)
        cart_a.save()
        return redirect("pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    coca_cola = Produto.objects.filter(nome="coca cola").values("valor")
    coca_cola_val = coca_cola[0]["valor"]
    coca_cola_obj = Produto.objects.get(nome="coca cola")
    coca_cola_cart = request.POST.get("total_cart")
    coca_cola_format = float(coca_cola_cart)
    if cart:
        cart.total += coca_cola_format
        print(cart.total)
        cart_a.produto.add()
        cart.save()
        return redirect("pedido")
    return redirect("pedido")


    