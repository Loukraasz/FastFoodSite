from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EnderecoForm, nameForm
from .models import User, Endereco as End

def index(request):
    form = nameForm()
    endereco = EnderecoForm()
    return render(request, "polls/index.html", {"form":form, "endereco":endereco})
def teste(request):
    form = nameForm(request.POST)
    endereco = EnderecoForm(request.POST)
       
    if form.is_valid() and endereco.is_valid():
        e = endereco.save()
        a = form.save(commit=False)
        a.adress_id = e.id
        a.save()
        e.save()
        return HttpResponse("salvo")
    return HttpResponse("pinto")