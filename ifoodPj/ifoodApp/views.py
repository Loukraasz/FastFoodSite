from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import nameForm

def index(request):
    form = nameForm()
    return render(request, "polls/index.html", {"form":form})
def teste(request):
    form = nameForm(request.POST)
    try:
        if form.is_valid():
            form.save()
            print("tentei")
            return render(request, "polls/teste.html")
    except ValueError or ValidationError:
        return HttpResponse("paia")
    return HttpResponse("pinto")