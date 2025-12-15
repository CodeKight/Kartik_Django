from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("Hello world")

def home(request):
    user = [

    {"name": "Ram Sharma", "age": 25, "address": "Kathmandu"},
    {"name": "Sita Rai", "age": 22, "address": "Pokhara"},
    {"name": "Hari Thapa", "age": 28, "address": "Lalitpur"},
    {"name": "Gita Karki", "age": 24, "address": "Bhaktapur"},
    {"name": "Nabin Adhikari", "age": 30, "address": "Chitwan"},
    {"name": "Asha Gurung", "age": 21, "address": "Butwal"},
    {"name": "Ramesh Poudel", "age": 35, "address": "Biratnagar"},
    {"name": "Mina Shrestha", "age": 27, "address": "Dharan"},
    {"name": "Kiran Joshi", "age": 29, "address": "Hetauda"},
    {"name": "Sunita Bhandari", "age": 26, "address": "Nepalgunj"}


]

    a="welcome to the page "
    context = {
        "title": "Homepage ",
        "first_line":a,
        "second_line":"This is home funciton. ",
        "people":user
    }
    return render(request, 'home.html',context)

def about_us(request):
    return HttpResponse("Hello about_us")

def contact(request):
    return HttpResponse("Hello contact")
