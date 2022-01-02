""" This module provides the function to register a model and customize an admin. """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    A Custom User Admin class for customizing the user admin interface.
    """

    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
        "age",
        "last_login",
        "is_staff",
        "is_active",
        "password",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
