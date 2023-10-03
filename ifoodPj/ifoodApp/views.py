from django.http import HttpResponse
from django.shortcuts import render
from .forms import nameForm

def index(request):
    form = nameForm()
    
    return render(request, "polls/index.html", {"form":form})
def teste(request):
    form = nameForm(request.POST)
    if form.is_valid():
        form.save()
        nome = form.data["username"]
        print(nome)
        return render(request, "polls/teste.html")
    
    return render(request, "polls/teste.html")