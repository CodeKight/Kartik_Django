from django.urls import path
from .views import first,home,about_us,contact, task # or *  #Import functions form views file

urlpatterns = [
    path('first/', first),
    path('home/', home),
    path('about_us/', about_us),
     path('contact/', contact),
     path('task/', task)
]


#OR, 
# from django.urls import path
# from . import views           #Import views file form current dir and then import fun using view.first 

# urlpatterns = [
#     path('first/', views.first),
#     path('home/', views.home),
#     path('about_us/', views.about_us),
#      path('contact/', views.contact)
# ]