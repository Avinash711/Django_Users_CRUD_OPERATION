from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','mobile'] #'date_joined'
                    #'is_active', 'is_staff','is_admin']
