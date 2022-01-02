""" This module provides the function to create a Uniform Resource Locator for signing up. """
from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
