""" This module provides the function to create a Uniform Resource Locator for the home page. """
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
