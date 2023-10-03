from django.http import HttpResponse
from django.shortcuts import render
from .forms import nameForm

def index(request):
    return HttpResponse("") 
