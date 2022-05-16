from django.contrib import admin
from .models import User


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'encrypted_password')
admin.site.register(User, UsersAdmin)

from django.contrib import admin
from .models import Employee


# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'title', 'email', 'facial_keypoints')
admin.site.register(Employee, EmployeesAdmin)

 