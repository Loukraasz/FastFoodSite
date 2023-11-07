from django.http import HttpResponse
from django.shortcuts import render
from .forms import EnderecoForm, NameForm

def index(request):
    user = NameForm()
    endereco = EnderecoForm()
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