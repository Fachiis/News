""" This module provides the function to create a user form object. """
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A Custom User Creation Form class for creating a user form object from the base UserCreationForm class.
    """

    class Meta(UserCreationForm.Meta):
        """Meta class for CustomUserCreationForm control."""

        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    """
    A Custom User Change Form class for updating a user form object from the base UserChangeForm class.
    """

    class Meta:
        """Meta class for CustomUserChangeForm control."""

        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "age",
        )
