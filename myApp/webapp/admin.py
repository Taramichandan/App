from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email' , 'phone' , 'address' ,'city', 'state','zip_code','created_at')

admin.site.register(Client,ClientAdmin)

# Register your models here.
