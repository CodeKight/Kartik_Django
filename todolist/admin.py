from django.contrib import admin
from .models import Todo



# Register your models here.


#admin.site.register(Todo) #if you don't want customization 

# @admin.register(Todo)  #if you want customization 
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'description']  # list or tupple [] or ()
    list_per_page = 10
    list_filter = ['status']
    search_fields = ('title', ) #Add a comma in case of tupple 
    list_editable = ('status',)
    

admin.site.register(Todo, TodoAdmin)