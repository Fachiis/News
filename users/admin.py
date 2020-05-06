from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#Django uses UserAdmin to render the nice admin look for User model. 
#Reasons for using UserAdim:
#1.UserAdmin uses UserChangeForm as the form to be used when modifying the object, 
#which in its turn uses User as its model.
#2.UserAdmin defines a formsets-property, later used by UserChangeForm, 
#which does not include your special fields.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        'first_name', 
        'last_name', 
        'username', 
        'email', 
        'age', 
        'last_login', 
        'is_staff', 
        'is_active', 
        'password',
        ]


admin.site.register(CustomUser, CustomUserAdmin)








