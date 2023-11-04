from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Endereco, nameForm

def index(request):
    form = nameForm()
    endereco = Endereco
    return render(request, "polls/index.html", {"form":form, "endereco":endereco})
def teste(request):
    form = nameForm(request.POST)
    endereco = Endereco(request.POST)
    if form.is_valid() and endereco.is_valid():
        endereco.save()
        form.save()
        return HttpResponse("salvo")
    return HttpResponse("pinto")