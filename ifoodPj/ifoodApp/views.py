from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import nameForm

def index(request):
    form = nameForm()
    return render(request, "polls/index.html", {"form":form})
def teste(request):
    form = nameForm(request.POST)
    print("ok")
    form.fields["username"].required = False
    if form.is_valid():
        print("teste")
        form.save()
        return HttpResponse("salvo")
    print("hummm")
    return HttpResponse("pinto")