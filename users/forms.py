from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#For us to be able to interact with the new user, we must provide a form to be used as signup 
#and that form is the UserCreationForm 
#and for us as admin to be enable updates the existing users, we also need a from which is
#the UserChangeForm
#Therefore, UserCreationForm---- for sign up by new users
#UserChangeForm----- for admin control over existing users
#We have to modify the two forms informing it about the added field

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    #This Meta class and Meta.fields help us to tell django to display the fields we want on the form
    #in the default user model plus our additional field we have as "age"
    #This default feilds that django will diplay is username, password1 and password2 for confirmation
    #To add the fields to be diplay we call out puple fields
    #Don't have to display the password1 and password2 fiedls as they are neccessary for the registration
    #of new users
    

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'age',
            )


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'age',
            )
