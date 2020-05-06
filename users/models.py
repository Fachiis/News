from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    #AbstractUser is a best choice as compare to AbstractBaseUser 
    #this is because if we just want to extent or add fields to the user model we already know
    #but using the later is quite complex as it will look as if we are just re-programming django again.
    #null is database-related while blank is form validation related
    age = models.PositiveIntegerField(null=True , blank=True)
    






