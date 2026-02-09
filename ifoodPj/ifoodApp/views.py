from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from ifoodApp import send_email
from .forms import EnderecoForm, NameForm
from .models import Pedido, Produto, Info, User ,Cart

def index(request):
    if request.method == "GET":
        global sessionUser
        request.session['session'] = "sessions"
        sessionUser = request.COOKIES.get("sessionid")
        user = User.objects.filter(sessionId=sessionUser).first()
        if user:
            return redirect("platform")
        return render(request, "polls/index.html",)
    email_login = request.POST.get("lEmail")
    password_login = request.POST.get("lPassword")
    users_email = User.objects.filter(email=email_login).first()
    try:
        if users_email :
            user = User.objects.get(email=email_login)
            password_user = user.password
            if password_user == password_login:
                session = request.COOKIES.get("sessionid")
                user.sessionId = session
                user.save()
                return redirect('platform')
    except ObjectDoesNotExist:
            return HttpResponse("usuario nao existe")
        

def cad(request):
    if request.method == "GET":
        user = NameForm()
        endereco = EnderecoForm()
        return render(request, "polls/cad.html", {"user": user, "endereco":endereco})
    if request.method == "POST":
        username = request.POST.get("username") 
        user = NameForm(request.POST)
        endereco = EnderecoForm(request.POST)
        if user.is_valid() and endereco.is_valid():
            user_exist = User.objects.filter(username=username).first()
            if user_exist:
                return HttpResponse("usuario ja existe")
            end_id = endereco.save()
            adress = user.save(commit=False)
            adress.adress_id = end_id.id
            adress.save()
            end_id.save()
            return redirect("index")
       


def rec_password(request):
    if request.method == "GET":
        return render(request, "polls/rec_password.html")
    email = request.POST.get("rec_email")
    try:
        global email_user
        email_user = User.objects.get(email=email)
        send_email.send_emails(email_user.email)
        return redirect("confirm_email")
    except ObjectDoesNotExist:
        return HttpResponse("pinto")
    
def confirm_email(request):
    if request.method == "GET":
        return render(request, "polls/confirm_email.html")
    code = request.POST.get("confirm_em")
    if code == send_email.final:
        return render(request, "polls/password_change.html")
    return HttpResponse("erro")

def password_change(request):
    if request.method == "GET":
        return render(request, "polls/password_change.html")
    np = request.POST.get("password")
    npc = request.POST.get("conf_password")
    if np == npc and np != None and npc != None:
        
        print(email_user.email)
        email_user.password = npc
        email_user.save()
        ok_pass = {"ok_pass":"senha alterada com sucesso"}
        return render(request, "polls/index.html", context=ok_pass)
    else:
        return HttpResponse("paia")
        
    
def pedido(request):
    if request.method == "GET":
        pass

def revisar_pedido(request):
    if request.method == "GET":
        user = request.COOKIES.get("sessionid")
        try:
            usuario = User.objects.get(sessionId=user)
            usuario_id = usuario.id
            cart = Cart.objects.get(cliente_id = usuario_id)
        except ObjectDoesNotExist:
            return redirect("index")
        info = Info.objects.filter(carrinho=cart.id).values("produto", "quantidade","total_p")
        counter = 0
        list_product = []
        list_quant = []
        list_price = []
        while counter < info.count():
            product = Produto.objects.filter(id=info[counter]["produto"]).values("nome")
            list_product.append(product[0]["nome"])
            quant = info[counter]["quantidade"]
            list_quant.append(quant)
            prices = info[counter]["total_p"]
            list_price.append(prices)
            counter += 1
        return render(request, "polls/revisar_pedido.html", context={"products": list_product, "prices":list_price,
                                                                 "quants":list_quant, "total":cart.total})
    user = request.COOKIES.get("sessionid")
    usuario = User.objects.get(sessionId=user)
    usuario_id = usuario.id
    cart = Cart.objects.get(cliente_id = usuario_id)
    pedido = Pedido(observacoes="", valor=cart.total ,status ="P" , cliente_id = usuario_id)
    info = Info.objects.filter(carrinho=cart.id)
    pedido.save()
    cart.delete()
    info.delete()
    return HttpResponse("finalizado")

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
            else:
                user = request.COOKIES.get("sessionid")
                try:
                    usuario = User.objects.get(sessionId=user)
                    usuario_id = usuario.id
                    cart = Cart.objects.get(cliente_id = usuario_id)
                except ObjectDoesNotExist:
                    return render(request, "polls/platform.html")
                info = Info.objects.filter(carrinho=cart.id).values("produto", "quantidade","total_p")
                counter = 0
                list_product = []
                list_quant = []
                list_price = []
                total_p = Info.objects.filter(carrinho=cart.id).values("produto").count()
                while counter < total_p:
                    product = Produto.objects.filter(id=info[counter]["produto"]).values("nome")
                    list_product.append(product[0]["nome"])
                    quant = info[counter]["quantidade"]
                    list_quant.append(quant)
                    prices = info[counter]["total_p"]
                    list_price.append(prices)
                    counter += 1
                return render(request, "polls/platform.html", context={"products": list_product, "prices":list_price,
                                                                 "quants":list_quant, "total":cart.total})
        except ObjectDoesNotExist:
            return render(request, "polls/index.html", relog)
    else:
        userP = request.COOKIES.get("sessionid")
        logUser = User.objects.get(sessionId=userP)
        logUser.sessionId = None
        logUser.save()
        return render(request, "polls/index.html")
    
def pizza_doce(request):
    return render(request , "polls/pizza_doce.html")


def refrigerantes(request):
    return render(request , "polls/refrigerantes.html")

def pizza(request):
    pass
    if request.method == "GET":
        pizza = Produto.objects.filter(nome="Pizza Calabresa").values("valor")
        pizza_val = pizza[0]["valor"]
        return render(request, "polls/pizza.html", {"product":pizza_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist or TypeError:
        pizza = Produto.objects.filter(nome="Pizza Calabresa").values("valor")
        pizza_obj = Produto.objects.get(nome="Pizza Calabresa")
        pizza_val_cart = request.POST.get("total_cart")
        pizza_val_format = float(pizza_val_cart)
        cart_a = Cart(total=pizza_val_format, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade= quant, produto=pizza_obj, carrinho=cart_a, total_p=pizza_val_format)
        quantidade.save()
        return redirect("revisar_pedido")
    pizza_obj = Produto.objects.get(nome="Pizza Calabresa")
    pizza_val_cart = request.POST.get("quant")
    print(pizza_val_cart + "sas")
    pizza_val_format = float(pizza_val_cart)
    if cart:
        cart.total += pizza_val_format 
        cart.save()
        quantidade = Info(quantidade= quant, produto=pizza_obj, carrinho=cart, total_p=pizza_val_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")


def temaki_salmao(request):
    pass
    if request.method == "GET":
        temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
        temaki_salmao_val = temaki_salmao[0]["valor"] 
        return render(request, "polls/temaki_salmao.html", {"product":temaki_salmao_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
        temaki_salmao_val = temaki_salmao[0]["valor"]
        temaki_obj = Produto.objects.get(nome="temaki de salmao")
        temaki_cart = request.POST.get("total_cart")
        temaki_format = float(temaki_cart)
        cart_a = Cart(total=temaki_salmao_val, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade= quant, produto=temaki_obj,carrinho=cart_a, total_p=temaki_format)
        quantidade.save()
        return redirect("revisar_pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    temaki_salmao = Produto.objects.filter(nome="temaki de salmao").values("valor")
    temaki_obj = Produto.objects.get(nome="temaki de salmao")
    temaki_cart = request.POST.get("total_cart")
    temaki_format = float(temaki_cart)
    if cart:
        cart.total += temaki_format
        cart.save()
        quantidade = Info(quantidade= quant, produto=temaki_obj, carrinho=cart, total_p=temaki_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")

def esfiha(request):
    pass
    if request.method == "GET":
        esfiha = Produto.objects.filter(nome="esfiha").values("valor")
        esfiha_val = esfiha[0]["valor"]
        return render(request, "polls/esfiha.html", {"product":esfiha_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        esfiha = Produto.objects.filter(nome="esfiha").values("valor")  
        esfiha_obj = Produto.objects.get(nome="esfiha")
        esfiha_cart = request.POST.get("total_cart")
        esfiha_format = float(esfiha_cart)
        cart_a = Cart(total=esfiha_format, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade= quant, produto=esfiha_obj, carrinho=cart_a, total_p=esfiha_format)
        quantidade.save()
        quantidade.carrinho.add(cart)
        return redirect("revisar_pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    esfiha = Produto.objects.filter(nome="esfiha").values("valor")
    esfiha_obj = Produto.objects.get(nome="esfiha")
    esfiha_cart = request.POST.get("total_cart")
    esfiha_format = float(esfiha_cart)
    if cart:
        cart.total += esfiha_format
        cart.save()
        quantidade = Info(quantidade= quant, produto=esfiha_obj, carrinho=cart, total_p=esfiha_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")


def sorvete(request):
    pass
    if request.method == "GET":
        sorvete = Produto.objects.filter(nome="sorvete").values("valor")
        sorvete_val = sorvete[0]["valor"]
        return render(request, "polls/sorvete.html", {"product":sorvete_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        sorvete = Produto.objects.filter(nome="sorvete").values("valor")
        sorvete_obj = Produto.objects.get(nome="sorvete")
        sorvete_cart = request.POST.get("total_cart")
        sorvete_format = float(sorvete_cart)
        cart_a = Cart(total=sorvete_format, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade= quant, produto=sorvete_obj, carrinho=cart_a, total_p=sorvete_format)
        quantidade.save()
        return redirect("revisar_pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    sorvete_obj = Produto.objects.get(nome="sorvete")
    sorvete_cart = request.POST.get("total_cart")
    sorvete_format = float(sorvete_cart)
    if cart:
        cart.total += sorvete_format
        cart.save()
        quantidade = Info(quantidade= quant, produto=sorvete_obj, carrinho=cart, total_p=sorvete_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")


def bolo(request):
    pass
    if request.method == "GET":
        bolo = Produto.objects.filter(nome="bolo").values("valor")
        bolo_val = bolo[0]["valor"]
        return render(request, "polls/bolo.html", {"product":bolo_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ValueError or ObjectDoesNotExist:
        bolo = Produto.objects.filter(nome="bolo").values("valor")     
        bolo_obj = Produto.objects.get(nome="bolo")
        bolo_cart = request.POST.get("total_cart")
        bolo_format = float(bolo_cart)
        cart_a = Cart(total=bolo_format, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade=quant, produto=bolo_obj, carrinho=cart_a, total_p=bolo_format)
        quantidade.save()
        return redirect("revisar_pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    bolo_obj = Produto.objects.get(nome="bolo")
    bolo_cart = request.POST.get("total_cart")
    bolo_format = float(bolo_cart)
    if cart:
        cart.total += bolo_format
        cart.save()
        quantidade = Info(quantidade= quant, produto=bolo_obj, carrinho=cart, total_p=bolo_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")


def coca_cola(request):
    pass
    if request.method == "GET":
        coca_cola = Produto.objects.filter(nome="coca cola").values("valor")
        coca_cola_val = coca_cola[0]["valor"]
        return render(request, "polls/coca_cola.html", {"product":coca_cola_val})
    quant = request.POST.get("quant")
    quant = int(quant)
    try:
        user = request.COOKIES.get("sessionid")
        usuario = User.objects.get(sessionId=user)
        cart = Cart.objects.get(cliente_id=usuario.id)
    except ObjectDoesNotExist:
        coca_cola = Produto.objects.filter(nome="coca cola").values("valor")
        coca_cola_obj = Produto.objects.get(nome="coca cola")
        coca_cola_cart = request.POST.get("total_cart")
        coca_cola_format = float(coca_cola_cart)
        cart_a = Cart(total=coca_cola_format, cliente_id=usuario.id)
        cart_a.save()
        quantidade = Info(quantidade= quant, produto=coca_cola_obj,carrinho = cart_a, total_p=coca_cola_format)
        quantidade.save()
        return redirect("revisar_pedido")
    cart = Cart.objects.get(cliente_id=usuario.id)
    coca_cola_obj = Produto.objects.get(nome="coca cola")
    coca_cola_cart = request.POST.get("total_cart")
    coca_cola_format = float(coca_cola_cart)
    if cart:
        cart.total += coca_cola_format
        cart.save()
        quantidade = Info(quantidade= quant, produto=coca_cola_obj,carrinho = cart, total_p=coca_cola_format)
        quantidade.save()
        return redirect("revisar_pedido")
    return redirect("revisar_pedido")


    