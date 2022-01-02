""" This module provides the function to create a user object. """
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A Custom User class for creating a user from the base AbstractUser class.

    New Field:
    age (int): The field column for adding user age.
    """

    age = models.PositiveIntegerField(null=True, blank=True)
