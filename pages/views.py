""" This module provides the business logic for the home page. """
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    A simple home page view class.
    """

    template_name = "home.html"
