from django.shortcuts import render
from django.http import HttpResponse
from .models import Info 

# Create your views here.

def info(request):
    return HttpResponse("Hello portfolio")