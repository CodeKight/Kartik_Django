from django.urls import path
from .views import first,home,about_us,contact

urlpatterns = [
    path('first/', first),
    path('home/', home),
    path('about_us/', about_us),
     path('contact/', contact)
]

