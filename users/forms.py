from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField() #cresting a new field called email in our custom form

    class Meta: # mention the model to which we want our form to interact with
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #list of fields in the desired order