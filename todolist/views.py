from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("Hello home")

def about_us(request):
    return HttpResponse("Hello about_us")

def contact(request):
    return HttpResponse("Hello contact")
