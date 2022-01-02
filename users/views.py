""" This module provides the business logic for creating a new user object. """
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """
    A Sign Up View class for creating a new user object from the base CreateView class.
    """
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")