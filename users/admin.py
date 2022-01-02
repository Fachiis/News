from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
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
